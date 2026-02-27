---
name: comfyui-official-docs
description: "Full-coverage ComfyUI official documentation skill using docs.comfy.org as the source of truth. Use when answering or implementing ComfyUI tasks that require official references: installation, interface behavior, workflow JSON, custom node development, registry publishing, Comfy Cloud usage, API endpoint details, request/response schemas, or troubleshooting. Use when users ask for latest official behavior, exact endpoint names, or citation-backed guidance."
---

# ComfyUI Official Docs

Use this skill to answer ComfyUI questions with official docs only, backed by a local full snapshot.

## Quick Start

1. Refresh the snapshot:
   `python3 scripts/sync_official_docs.py --clean`
2. Fast refresh with incremental cache reuse:
   `python3 scripts/sync_official_docs.py`
3. Audit full-coverage integrity:
   `python3 scripts/audit_snapshot.py`
4. Search relevant pages:
   `python3 scripts/search_official_docs.py "your query" --top 15`
5. Read matched files under `references/docs/`.
6. Cite exact official URLs from `references/docs-manifest.tsv`.

## Workflow

1. Determine whether freshness matters.
   For "latest", "new", "recent", API behavior, or cloud features, run sync first.
2. Locate candidate pages.
   Use `scripts/search_official_docs.py` for keyword retrieval.
   Use `--lang en` or `--lang zh` when you want language-specific matches.
   Use `--section api-reference` (or other top-level section) to narrow scope.
   Default behavior suppresses lowercase `zh-cn` alias duplicates when identical to canonical pages.
3. Validate against source records.
   Confirm URL mapping in `references/docs-manifest.tsv` and last sync status in `references/snapshot-metadata.json`.
4. Answer with citations.
   Provide the final answer with official docs URLs and keep wording consistent with docs.

## Coverage Contract

Treat full coverage as satisfied only when:

1. `references/sitemap.xml` is present.
2. `references/docs-manifest.tsv` exists for all sitemap entries.
3. `references/snapshot-metadata.json` reports `coverage_complete = true`.
4. `references/docs/` contains markdown pages mapped by manifest paths.
5. `python3 scripts/audit_snapshot.py` returns exit code `0`.

If coverage is incomplete, rerun:

`python3 scripts/sync_official_docs.py --clean --workers 8 --retries 5`

For intentionally partial snapshots (debug/sampling only), opt in explicitly:

`python3 scripts/sync_official_docs.py --limit 20 --allow-partial`

To force full re-download and bypass cache:

`python3 scripts/sync_official_docs.py --clean --no-incremental`

Sync writes through a staging directory and atomically swaps on success.
Use `--no-atomic` only for debugging.

## Reference Files

- `references/sitemap.xml`: official page inventory.
- `references/llms.txt`: official docs index links.
- `references/llms-full.txt`: single-file consolidated docs text.
- `references/docs/`: per-page markdown mirror from official `.md` endpoints.
- `references/docs-manifest.tsv`: URL to local-file mapping and sync status.
- `references/snapshot-metadata.json`: sync metadata and error summary.
- `references/coverage.md`: section counts and failed page list (if any).
- `scripts/audit_snapshot.py`: strict completeness and integrity audit.

## Operating Rules

1. Prefer official docs.comfy.org content over memory.
2. Do not mix unofficial community guidance unless explicitly requested.
3. Report exact page URLs for endpoint-level or behavior-critical claims.
4. Mention snapshot date when answering "latest" questions.
