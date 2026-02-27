#!/usr/bin/env python3
"""Sync official ComfyUI documentation from docs.comfy.org.

This script downloads:
1) sitemap.xml
2) llms.txt
3) llms-full.txt
4) Every page from sitemap.xml as markdown (<page>.md)

Output is written under the skill's references/ directory.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import sys
import threading
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

BASE_URL = "https://docs.comfy.org"
BASE_HOST = urlparse(BASE_URL).netloc.lower()
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
LLMS_INDEX_URL = f"{BASE_URL}/llms.txt"
LLMS_FULL_URL = f"{BASE_URL}/llms-full.txt"
USER_AGENT = "comfyui-official-docs-skill/1.0"
SAFE_SEGMENT_RE = re.compile(r"[^a-zA-Z0-9._-]+")


@dataclass
class PageEntry:
    url: str
    lastmod: str


@dataclass
class DownloadResult:
    url: str
    md_url: str
    lastmod: str
    local_path: str
    status: str
    fetch_mode: str
    bytes_count: int
    sha256: str
    duration_ms: int
    error: str


def fetch_bytes(url: str, timeout: int, retries: int, retry_delay: float) -> bytes:
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        request = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/plain,text/markdown,application/xml,text/xml,*/*",
            },
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read()
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_exc = exc
            if attempt < retries:
                time.sleep(retry_delay * attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_exc}") from last_exc


def decode_payload(payload: bytes) -> str:
    try:
        return payload.decode("utf-8")
    except UnicodeDecodeError:
        return payload.decode("utf-8", errors="replace")


def is_official_docs_url(url: str) -> bool:
    parsed = urlparse(url.strip())
    return parsed.scheme in {"https", "http"} and parsed.netloc.lower() == BASE_HOST


def parse_sitemap(xml_text: str) -> List[PageEntry]:
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_text)
    items: Dict[str, PageEntry] = {}
    for node in root.findall("sm:url", namespace):
        loc = (node.findtext("sm:loc", default="", namespaces=namespace) or "").strip()
        if not is_official_docs_url(loc):
            continue
        lastmod = (
            node.findtext("sm:lastmod", default="", namespaces=namespace) or ""
        ).strip()
        items[loc] = PageEntry(url=loc, lastmod=lastmod)
    return sorted(items.values(), key=lambda item: item.url)


def sanitize_segment(segment: str) -> str:
    cleaned = SAFE_SEGMENT_RE.sub("-", segment.strip())
    cleaned = cleaned.strip("-._")
    return cleaned or "item"


def url_to_relpath(url: str) -> Path:
    parsed = urlparse(url)
    raw_path = unquote(parsed.path).strip("/")
    if not raw_path:
        return Path("index.md")

    if raw_path.endswith(".md"):
        raw_path = raw_path[:-3]

    segments = [sanitize_segment(part) for part in raw_path.split("/") if part]
    if not segments:
        segments = ["index"]
    return Path(*segments).with_suffix(".md")


def to_markdown_url(url: str) -> str:
    cleaned = url.rstrip("/")
    if cleaned == BASE_URL:
        cleaned = f"{BASE_URL}/index"
    if cleaned.endswith(".md"):
        return cleaned
    return f"{cleaned}.md"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_int(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def load_manifest_rows_by_url(manifest_path: Path) -> Dict[str, Dict[str, str]]:
    if not manifest_path.exists():
        return {}
    lines = manifest_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return {}

    headers = lines[0].split("\t")
    col = {name: idx for idx, name in enumerate(headers)}
    required = {"url", "local_path", "status", "lastmod"}
    if not required.issubset(col):
        return {}

    by_url: Dict[str, Dict[str, str]] = {}
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) < len(headers):
            parts += [""] * (len(headers) - len(parts))
        row = {name: parts[idx] for name, idx in col.items()}
        url = row.get("url", "")
        if url:
            by_url[url] = row
    return by_url


def try_build_cached_result(
    entry: PageEntry,
    source_docs_dir: Path,
    target_docs_dir: Path,
    existing_row: Dict[str, str],
) -> DownloadResult | None:
    if existing_row.get("status") != "ok":
        return None
    if existing_row.get("lastmod", "") != entry.lastmod:
        return None

    rel_path = existing_row.get("local_path", "") or str(url_to_relpath(entry.url).as_posix())
    source = source_docs_dir / rel_path
    if not source.exists():
        return None
    target = target_docs_dir / rel_path
    if source != target:
        try:
            link_or_copy_file(source, target)
        except OSError:
            return None

    bytes_count = parse_int(existing_row.get("bytes", "0"))
    if bytes_count <= 0:
        try:
            bytes_count = source.stat().st_size
        except OSError:
            bytes_count = 0

    return DownloadResult(
        url=entry.url,
        md_url=to_markdown_url(entry.url),
        lastmod=entry.lastmod,
        local_path=rel_path,
        status="ok",
        fetch_mode="cached",
        bytes_count=bytes_count,
        sha256=existing_row.get("sha256", ""),
        duration_ms=0,
        error="",
    )


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True))


def make_staging_dir(target_references_dir: Path) -> Path:
    parent = target_references_dir.parent
    base = target_references_dir.name
    for attempt in range(100):
        stamp = int(time.time() * 1000)
        candidate = parent / f".{base}.staging-{stamp}-{os.getpid()}-{attempt}"
        if not candidate.exists():
            candidate.mkdir(parents=True, exist_ok=False)
            return candidate
    raise RuntimeError(f"Unable to allocate staging directory near {target_references_dir}")


def link_or_copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def atomic_swap_directory(staging_dir: Path, live_dir: Path) -> None:
    if not staging_dir.exists():
        raise RuntimeError(f"Staging directory does not exist: {staging_dir}")

    backup_dir: Path | None = None
    if live_dir.exists():
        for attempt in range(100):
            stamp = int(time.time() * 1000)
            candidate = live_dir.parent / f".{live_dir.name}.backup-{stamp}-{os.getpid()}-{attempt}"
            if not candidate.exists():
                backup_dir = candidate
                break
        if backup_dir is None:
            raise RuntimeError(f"Atomic swap error [backup-alloc]: unable to allocate backup near {live_dir}")
        try:
            live_dir.rename(backup_dir)
        except OSError as exc:
            raise RuntimeError(
                "Atomic swap error [backup-rename]: "
                f"cannot move live directory {live_dir} -> {backup_dir}: {exc}"
            ) from exc

    try:
        staging_dir.rename(live_dir)
    except OSError as swap_exc:
        rollback_exc: OSError | None = None
        if backup_dir is not None and backup_dir.exists():
            try:
                backup_dir.rename(live_dir)
            except OSError as exc:
                rollback_exc = exc
        if rollback_exc is not None:
            raise RuntimeError(
                "Atomic swap error [swap-rename+rollback-failed]: "
                f"cannot move staging {staging_dir} -> {live_dir}; rollback also failed "
                f"{backup_dir} -> {live_dir}: {rollback_exc}"
            ) from swap_exc
        raise RuntimeError(
            "Atomic swap error [swap-rename]: "
            f"cannot move staging {staging_dir} -> {live_dir}; live directory restored from backup"
        ) from swap_exc
    else:
        if backup_dir is not None and backup_dir.exists():
            try:
                shutil.rmtree(backup_dir)
            except OSError as exc:
                raise RuntimeError(
                    "Atomic swap error [backup-cleanup]: "
                    f"swap succeeded but failed to remove backup {backup_dir}: {exc}"
                ) from exc


def download_page(
    entry: PageEntry,
    docs_dir: Path,
    timeout: int,
    retries: int,
    retry_delay: float,
) -> DownloadResult:
    md_url = to_markdown_url(entry.url)
    rel_path = url_to_relpath(entry.url)
    target = docs_dir / rel_path
    start = time.time()

    try:
        payload = fetch_bytes(md_url, timeout=timeout, retries=retries, retry_delay=retry_delay)
        text = decode_payload(payload)
        write_text(target, text)
        duration_ms = int((time.time() - start) * 1000)
        return DownloadResult(
            url=entry.url,
            md_url=md_url,
            lastmod=entry.lastmod,
            local_path=str(rel_path.as_posix()),
            status="ok",
            fetch_mode="downloaded",
            bytes_count=len(text.encode("utf-8")),
            sha256=sha256_text(text),
            duration_ms=duration_ms,
            error="",
        )
    except Exception as exc:  # broad: we want a full report, not hard-fail.
        duration_ms = int((time.time() - start) * 1000)
        return DownloadResult(
            url=entry.url,
            md_url=md_url,
            lastmod=entry.lastmod,
            local_path=str(rel_path.as_posix()),
            status="error",
            fetch_mode="error",
            bytes_count=0,
            sha256="",
            duration_ms=duration_ms,
            error=str(exc),
        )


def write_manifest(path: Path, results: List[DownloadResult]) -> None:
    headers = [
        "url",
        "md_url",
        "lastmod",
        "local_path",
        "status",
        "fetch_mode",
        "bytes",
        "sha256",
        "duration_ms",
        "error",
    ]
    lines = ["\t".join(headers)]
    for item in sorted(results, key=lambda r: r.url):
        lines.append(
            "\t".join(
                [
                    item.url,
                    item.md_url,
                    item.lastmod,
                    item.local_path,
                    item.status,
                    item.fetch_mode,
                    str(item.bytes_count),
                    item.sha256,
                    str(item.duration_ms),
                    item.error.replace("\t", " ").replace("\n", " "),
                ]
            )
        )
    write_text(path, "\n".join(lines) + "\n")


def write_coverage_report(path: Path, results: List[DownloadResult]) -> None:
    section_counts: Dict[str, int] = {}
    failures = [item for item in results if item.status == "error"]
    skipped = [item for item in results if item.status == "skipped"]
    downloaded = [item for item in results if item.fetch_mode == "downloaded"]
    cached = [item for item in results if item.fetch_mode == "cached"]
    ok_count = len([item for item in results if item.status == "ok"])
    for item in results:
        rel = item.local_path
        section = rel.split("/", 1)[0]
        section_counts[section] = section_counts.get(section, 0) + 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# ComfyUI Official Docs Coverage",
        "",
        f"- Snapshot time: `{now}`",
        f"- Total pages in sitemap: `{len(results)}`",
        f"- Downloaded successfully: `{ok_count}`",
        f"- Downloaded from network: `{len(downloaded)}`",
        f"- Reused cached pages: `{len(cached)}`",
        f"- Failed downloads: `{len(failures)}`",
        f"- Skipped pages: `{len(skipped)}`",
        "",
        "## Top-Level Section Counts",
        "",
        "| Section | Pages |",
        "|---|---:|",
    ]
    for section, count in sorted(section_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {section} | {count} |")

    if failures:
        lines.extend(
            [
                "",
                "## Failed Pages",
                "",
                "| URL | Error |",
                "|---|---|",
            ]
        )
        for item in failures[:200]:
            error = item.error.replace("|", "\\|")
            lines.append(f"| {item.url} | {error} |")

    if skipped:
        lines.extend(
            [
                "",
                "## Skipped Pages",
                "",
                "| URL | Reason |",
                "|---|---|",
            ]
        )
        for item in skipped[:200]:
            reason = item.error.replace("|", "\\|")
            lines.append(f"| {item.url} | {reason} |")

    write_text(path, "\n".join(lines) + "\n")


def build_snapshot(
    references_dir: Path,
    workers: int,
    timeout: int,
    retries: int,
    retry_delay: float,
    limit: int,
    clean: bool,
    skip_pages: bool,
    allow_partial: bool,
    incremental: bool,
    atomic: bool,
) -> int:
    live_references_dir = references_dir.resolve()
    staging_dir: Path | None = None
    work_references_dir = live_references_dir

    if atomic:
        staging_dir = make_staging_dir(live_references_dir)
        work_references_dir = staging_dir
    else:
        work_references_dir.mkdir(parents=True, exist_ok=True)

    try:
        docs_dir = work_references_dir / "docs"
        manifest_path = work_references_dir / "docs-manifest.tsv"
        if clean and not atomic and docs_dir.exists():
            shutil.rmtree(docs_dir)
        docs_dir.mkdir(parents=True, exist_ok=True)

        sitemap_xml = decode_payload(fetch_bytes(SITEMAP_URL, timeout, retries, retry_delay))
        llms_index_text = decode_payload(fetch_bytes(LLMS_INDEX_URL, timeout, retries, retry_delay))
        llms_full_text = decode_payload(fetch_bytes(LLMS_FULL_URL, timeout, retries, retry_delay))

        write_text(work_references_dir / "sitemap.xml", sitemap_xml)
        write_text(work_references_dir / "llms.txt", llms_index_text)
        write_text(work_references_dir / "llms-full.txt", llms_full_text)

        entries = parse_sitemap(sitemap_xml)
        if limit > 0:
            entries = entries[:limit]

        existing_by_url: Dict[str, Dict[str, str]] = {}
        cache_source_dir = live_references_dir / "docs"
        if incremental and not clean and not skip_pages:
            try:
                existing_by_url = load_manifest_rows_by_url(live_references_dir / "docs-manifest.tsv")
            except OSError:
                existing_by_url = {}

        results: List[DownloadResult] = []
        if skip_pages:
            for entry in entries:
                rel_path = str(url_to_relpath(entry.url).as_posix())
                results.append(
                    DownloadResult(
                        url=entry.url,
                        md_url=to_markdown_url(entry.url),
                        lastmod=entry.lastmod,
                        local_path=rel_path,
                        status="skipped",
                        fetch_mode="skipped",
                        bytes_count=0,
                        sha256="",
                        duration_ms=0,
                        error="skip-pages enabled",
                    )
                )
        else:
            entries_to_download: List[PageEntry] = []
            if existing_by_url:
                for entry in entries:
                    cached = try_build_cached_result(
                        entry,
                        cache_source_dir,
                        docs_dir,
                        existing_by_url.get(entry.url, {}),
                    )
                    if cached is not None:
                        results.append(cached)
                    else:
                        entries_to_download.append(entry)
            else:
                entries_to_download = entries

            total = len(entries)
            counter = len(results)
            lock = threading.Lock()
            if counter > 0:
                print(f"[sync] reused cache for {counter}/{total} pages", file=sys.stderr)

            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                future_to_entry = {
                    executor.submit(
                        download_page,
                        entry,
                        docs_dir,
                        timeout,
                        retries,
                        retry_delay,
                    ): entry
                    for entry in entries_to_download
                }
                for future in concurrent.futures.as_completed(future_to_entry):
                    result = future.result()
                    results.append(result)
                    with lock:
                        counter += 1
                        if counter % 25 == 0 or counter == total:
                            print(f"[sync] {counter}/{total} pages processed", file=sys.stderr)

        write_manifest(manifest_path, results)
        write_coverage_report(work_references_dir / "coverage.md", results)

        ok_count = len([item for item in results if item.status == "ok"])
        skipped_count = len([item for item in results if item.status == "skipped"])
        downloaded_count = len([item for item in results if item.fetch_mode == "downloaded"])
        cached_count = len([item for item in results if item.fetch_mode == "cached"])
        error_items = [item for item in results if item.status == "error"]
        coverage_complete = (
            len(entries) > 0
            and ok_count == len(entries)
            and len(error_items) == 0
            and skipped_count == 0
            and not skip_pages
            and limit == 0
        )
        partial_reasons: List[str] = []
        if limit > 0:
            partial_reasons.append(f"limit={limit}")
        if skip_pages:
            partial_reasons.append("skip_pages=true")
        if skipped_count:
            partial_reasons.append(f"skipped={skipped_count}")
        if ok_count != len(entries):
            partial_reasons.append(f"ok={ok_count}/entries={len(entries)}")

        snapshot = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "base_url": BASE_URL,
            "sources": {
                "sitemap_xml": SITEMAP_URL,
                "llms_index": LLMS_INDEX_URL,
                "llms_full": LLMS_FULL_URL,
            },
            "totals": {
                "entries": len(entries),
                "ok": ok_count,
                "downloaded": downloaded_count,
                "cached": cached_count,
                "skipped": skipped_count,
                "errors": len(error_items),
                "workers": workers,
                "timeout_seconds": timeout,
                "retries": retries,
                "limit": limit,
            },
            "coverage_complete": coverage_complete,
            "allow_partial": allow_partial,
            "incremental": incremental,
            "atomic": atomic,
            "partial_reasons": partial_reasons,
            "errors": [
                {"url": item.url, "md_url": item.md_url, "error": item.error}
                for item in error_items[:200]
            ],
        }
        write_json(work_references_dir / "snapshot-metadata.json", snapshot)

        print(
            "[sync] done "
            f"(entries={len(entries)}, ok={ok_count}, downloaded={downloaded_count}, "
            f"cached={cached_count}, skipped={skipped_count}, "
            f"errors={len(error_items)}, refs={live_references_dir})"
        )
        if error_items:
            return_code = 2
        elif not allow_partial and not coverage_complete:
            reason_text = ", ".join(partial_reasons) if partial_reasons else "unknown partial state"
            print(
                "[sync] incomplete coverage detected: "
                f"{reason_text}. Re-run without --limit/--skip-pages, or use --allow-partial.",
                file=sys.stderr,
            )
            return_code = 3
        else:
            return_code = 0

        if atomic and return_code == 0 and staging_dir is not None:
            print(
                f"[sync] atomic swap start (staging={staging_dir}, live={live_references_dir})",
                file=sys.stderr,
            )
            try:
                atomic_swap_directory(staging_dir, live_references_dir)
            except RuntimeError as exc:
                print(f"[sync] atomic swap failed: {exc}", file=sys.stderr)
                return 4
            staging_dir = None
            print("[sync] atomic swap complete", file=sys.stderr)

        return return_code
    finally:
        if staging_dir is not None and staging_dir.exists():
            shutil.rmtree(staging_dir, ignore_errors=True)


def parse_args() -> argparse.Namespace:
    default_refs = Path(__file__).resolve().parents[1] / "references"
    parser = argparse.ArgumentParser(
        description="Sync full official docs.comfy.org markdown snapshot into references/."
    )
    parser.add_argument(
        "--references-dir",
        default=str(default_refs),
        help="Target references directory (default: skill references/).",
    )
    parser.add_argument("--workers", type=int, default=16, help="Concurrent download workers.")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds.")
    parser.add_argument("--retries", type=int, default=3, help="Retry count per request.")
    parser.add_argument(
        "--retry-delay", type=float, default=1.0, help="Base delay between retries in seconds."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Only process first N sitemap entries (0 means all).",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete existing references/docs/ before downloading.",
    )
    parser.add_argument(
        "--skip-pages",
        action="store_true",
        help="Fetch only sitemap.xml + llms files and skip page downloads.",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Allow partial snapshots (e.g. --limit or --skip-pages) to exit successfully.",
    )
    parser.set_defaults(incremental=True)
    parser.add_argument(
        "--no-incremental",
        action="store_false",
        dest="incremental",
        help="Disable manifest cache reuse and re-download selected pages.",
    )
    parser.set_defaults(atomic=True)
    parser.add_argument(
        "--no-atomic",
        action="store_false",
        dest="atomic",
        help="Write directly to references dir instead of staging + atomic swap.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return build_snapshot(
        references_dir=Path(args.references_dir).resolve(),
        workers=max(args.workers, 1),
        timeout=max(args.timeout, 5),
        retries=max(args.retries, 1),
        retry_delay=max(args.retry_delay, 0.1),
        limit=max(args.limit, 0),
        clean=bool(args.clean),
        skip_pages=bool(args.skip_pages),
        allow_partial=bool(args.allow_partial),
        incremental=bool(args.incremental),
        atomic=bool(args.atomic),
    )


if __name__ == "__main__":
    raise SystemExit(main())
