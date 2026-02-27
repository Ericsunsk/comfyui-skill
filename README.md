# ComfyUI Official Docs Skill

A full-coverage Codex skill for ComfyUI official documentation, using `https://docs.comfy.org` as the source of truth.

## What This Project Does

- Syncs official docs into a local snapshot (`references/`).
- Audits snapshot integrity and coverage.
- Searches local markdown pages quickly for retrieval and citation.
- Preserves snapshot consistency with atomic sync (staging + swap).

## Project Layout

- `SKILL.md`: skill instructions and operating contract.
- `agents/openai.yaml`: agent wiring configuration.
- `scripts/sync_official_docs.py`: fetch and build snapshot.
- `scripts/audit_snapshot.py`: strict coverage/integrity check.
- `scripts/search_official_docs.py`: local doc search.
- `references/`: synced official docs and metadata.

## Quick Start

```bash
# 1) Full refresh
python3 scripts/sync_official_docs.py --clean

# 2) Fast incremental refresh (cache reuse)
python3 scripts/sync_official_docs.py

# 3) Integrity audit
python3 scripts/audit_snapshot.py

# 4) Search
python3 scripts/search_official_docs.py "your query" --top 10
```

## Search Tips

```bash
# Language / section filters
python3 scripts/search_official_docs.py "add tags to asset" --lang en --section api-reference --top 5

# Machine-readable output
python3 scripts/search_official_docs.py "workflow json" --json
```

## Snapshot Completeness Contract

Treat coverage as complete only when all conditions are true:

1. `references/sitemap.xml` exists.
2. `references/docs-manifest.tsv` exists and maps sitemap URLs.
3. `references/snapshot-metadata.json` reports `coverage_complete = true`.
4. `references/docs/` contains mapped markdown pages.
5. `python3 scripts/audit_snapshot.py` exits `0`.

## Recent Reliability Improvements

- **Atomic sync by default**: writes into a staging directory and swaps into live snapshot only after success.
- **Failure isolation**: failed sync does not corrupt live snapshot.
- **Structured swap errors**: atomic swap now emits stage-specific error categories.
- **Cleaner snippets**: search suppresses Mintlify index preamble noise lines.
- **Better relevance**: search now downweights stopwords/short noise terms and boosts title matches.

## Source Policy

- Official docs only (`docs.comfy.org`) unless explicitly requested otherwise.
- For behavior-critical answers, cite exact official page URLs from `docs-manifest.tsv`.
