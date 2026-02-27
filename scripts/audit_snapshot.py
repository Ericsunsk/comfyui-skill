#!/usr/bin/env python3
"""Audit a local ComfyUI docs snapshot for completeness and consistency."""

from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Dict, List, Set


def parse_manifest(manifest_path: Path) -> List[Dict[str, str]]:
    lines = manifest_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError("manifest is empty")

    headers = lines[0].split("\t")
    col = {name: idx for idx, name in enumerate(headers)}
    required = {"url", "local_path", "status"}
    missing = required - set(col)
    if missing:
        raise ValueError(f"manifest missing required columns: {', '.join(sorted(missing))}")

    rows: List[Dict[str, str]] = []
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) < len(headers):
            parts += [""] * (len(headers) - len(parts))
        rows.append({name: parts[idx] for name, idx in col.items()})
    return rows


def parse_sitemap_urls(sitemap_path: Path) -> Set[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(sitemap_path.read_text(encoding="utf-8"))
    urls: Set[str] = set()
    for node in root.findall("sm:url", ns):
        loc = (node.findtext("sm:loc", default="", namespaces=ns) or "").strip()
        if loc:
            urls.add(loc)
    return urls


def load_snapshot_metadata(path: Path) -> Dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit references snapshot integrity.")
    parser.add_argument(
        "--references-dir",
        default=str(Path(__file__).resolve().parents[1] / "references"),
        help="References directory containing docs-manifest.tsv and docs/.",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Do not fail when skipped/error/partial conditions are detected.",
    )
    args = parser.parse_args()

    references_dir = Path(args.references_dir).resolve()
    docs_dir = references_dir / "docs"
    manifest_path = references_dir / "docs-manifest.tsv"
    sitemap_path = references_dir / "sitemap.xml"
    metadata_path = references_dir / "snapshot-metadata.json"

    failures: List[str] = []
    warnings: List[str] = []

    if not references_dir.exists():
        print(f"FAIL: references directory not found: {references_dir}")
        return 2

    if not docs_dir.exists():
        failures.append(f"missing docs directory: {docs_dir}")
    if not manifest_path.exists():
        failures.append(f"missing manifest: {manifest_path}")
    if not sitemap_path.exists():
        failures.append(f"missing sitemap: {sitemap_path}")

    rows: List[Dict[str, str]] = []
    if manifest_path.exists():
        try:
            rows = parse_manifest(manifest_path)
        except Exception as exc:  # noqa: BLE001 - explicit audit error message
            failures.append(f"manifest parse failed: {exc}")

    status_counts = Counter(row.get("status", "") for row in rows)
    ok_rows = [row for row in rows if row.get("status") == "ok"]
    error_rows = [row for row in rows if row.get("status") == "error"]
    skipped_rows = [row for row in rows if row.get("status") == "skipped"]

    manifest_urls = [row.get("url", "") for row in rows]
    manifest_paths = [row.get("local_path", "") for row in rows]

    duplicate_urls = [url for url, cnt in Counter(manifest_urls).items() if url and cnt > 1]
    duplicate_paths = [p for p, cnt in Counter(manifest_paths).items() if p and cnt > 1]
    if duplicate_urls:
        failures.append(f"duplicate urls in manifest: {len(duplicate_urls)}")
    if duplicate_paths:
        failures.append(f"duplicate local paths in manifest: {len(duplicate_paths)}")

    missing_ok_files = []
    if docs_dir.exists():
        for row in ok_rows:
            rel = row.get("local_path", "")
            if not rel:
                failures.append("ok row with empty local_path")
                continue
            if not (docs_dir / rel).exists():
                missing_ok_files.append(rel)
    if missing_ok_files:
        failures.append(f"ok rows missing files: {len(missing_ok_files)}")

    sitemap_urls: Set[str] = set()
    if sitemap_path.exists():
        try:
            sitemap_urls = parse_sitemap_urls(sitemap_path)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"sitemap parse failed: {exc}")

    strict_full = not args.allow_partial

    if sitemap_urls and rows:
        manifest_url_set = set(manifest_urls)
        missing_in_manifest = sitemap_urls - manifest_url_set
        extra_in_manifest = manifest_url_set - sitemap_urls
        if missing_in_manifest:
            if strict_full:
                failures.append(f"sitemap urls missing from manifest: {len(missing_in_manifest)}")
            else:
                warnings.append(f"sitemap urls missing from manifest: {len(missing_in_manifest)}")
        if extra_in_manifest:
            failures.append(f"manifest urls not present in sitemap: {len(extra_in_manifest)}")

    metadata = {}
    if metadata_path.exists():
        try:
            metadata = load_snapshot_metadata(metadata_path)
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"snapshot metadata parse failed: {exc}")
    else:
        warnings.append("snapshot-metadata.json is missing")

    if metadata:
        totals = metadata.get("totals", {})
        if isinstance(totals, dict):
            if rows and totals.get("entries") != len(rows):
                warnings.append(
                    f"metadata totals.entries={totals.get('entries')} != manifest rows={len(rows)}"
                )
            if totals.get("ok") is not None and totals.get("ok") != len(ok_rows):
                warnings.append(f"metadata totals.ok={totals.get('ok')} != ok rows={len(ok_rows)}")
            if totals.get("downloaded") is not None:
                downloaded_rows = len([r for r in rows if r.get("fetch_mode") == "downloaded"])
                if totals.get("downloaded") != downloaded_rows:
                    warnings.append(
                        "metadata totals.downloaded="
                        f"{totals.get('downloaded')} != downloaded rows={downloaded_rows}"
                    )
            if totals.get("cached") is not None:
                cached_rows = len([r for r in rows if r.get("fetch_mode") == "cached"])
                if totals.get("cached") != cached_rows:
                    warnings.append(
                        f"metadata totals.cached={totals.get('cached')} != cached rows={cached_rows}"
                    )
            if totals.get("errors") is not None and totals.get("errors") != len(error_rows):
                warnings.append(
                    f"metadata totals.errors={totals.get('errors')} != error rows={len(error_rows)}"
                )
            if totals.get("skipped") is not None and totals.get("skipped") != len(skipped_rows):
                warnings.append(
                    f"metadata totals.skipped={totals.get('skipped')} != skipped rows={len(skipped_rows)}"
                )

    if strict_full:
        if not rows:
            failures.append("manifest has no rows")
        if error_rows:
            failures.append(f"strict mode disallows error rows: {len(error_rows)}")
        if skipped_rows:
            failures.append(f"strict mode disallows skipped rows: {len(skipped_rows)}")
        if sitemap_urls and len(rows) != len(sitemap_urls):
            failures.append(
                f"strict mode requires manifest rows == sitemap urls ({len(rows)} != {len(sitemap_urls)})"
            )
        if sitemap_urls and len(ok_rows) != len(sitemap_urls):
            failures.append(
                f"strict mode requires ok rows == sitemap urls ({len(ok_rows)} != {len(sitemap_urls)})"
            )

    print(f"Snapshot dir: {references_dir}")
    print(f"Manifest rows: {len(rows)}")
    print(f"Status counts: {dict(status_counts)}")
    if sitemap_urls:
        print(f"Sitemap urls: {len(sitemap_urls)}")
    print(f"Strict mode: {strict_full}")

    if warnings:
        print("")
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("")
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        if missing_ok_files:
            print(f"- sample missing files: {missing_ok_files[:10]}")
        return 2

    print("")
    print("Audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
