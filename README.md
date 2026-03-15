# ComfyUI Official Docs Skill

An official-docs-backed Codex skill for ComfyUI, using a local full snapshot of `https://docs.comfy.org` as the source of truth.

## What This Project Does

- Syncs official docs into a local snapshot (`references/`).
- Audits snapshot integrity and coverage.
- Searches local markdown pages with task-aware routing for retrieval and citation.
- Helps agents route ComfyUI tasks into the right official doc families.
- Preserves snapshot consistency with atomic sync (staging + swap).

## Project Layout

- `SKILL.md`: skill instructions and operating contract.
- `agents/openai.yaml`: agent wiring configuration.
- `scripts/sync_official_docs.py`: fetch and build snapshot.
- `scripts/audit_snapshot.py`: strict coverage/integrity check.
- `scripts/search_official_docs.py`: local doc search with `--task` presets.
- `references/task-routing.md`: curated task-to-doc-family entrypoints.
- `references/`: synced official docs and metadata.

## Quick Start

```bash
# 1) Search the current snapshot by task
python3 scripts/search_official_docs.py "queue prompt websocket routes" --task server --top 8
python3 scripts/search_official_docs.py "workflow json schema" --task workflow --top 8
python3 scripts/search_official_docs.py "publish node version" --task registry --top 8

# 2) Refresh only when freshness matters or the snapshot is missing
python3 scripts/sync_official_docs.py

# 3) Full refresh when you need a clean rebuild
python3 scripts/sync_official_docs.py --clean

# 4) Integrity audit
python3 scripts/audit_snapshot.py
```

## Search Tips

```bash
# Built-in node lookup
python3 scripts/search_official_docs.py "KSampler" --task node --section built-in-nodes --top 5

# Cloud API lookup
python3 scripts/search_official_docs.py "submit workflow execution" --task cloud --top 5

# Language / section filters still work
python3 scripts/search_official_docs.py "add tags to asset" --task cloud --lang en --section api-reference --top 5

# Machine-readable output
python3 scripts/search_official_docs.py "workflow json" --task workflow --json
```

See `references/task-routing.md` for the recommended starting pages and search patterns by task family.

## Task Families

- `workflow`: workflow design, built-in nodes, templates, and workflow JSON schema.
- `node`: official built-in node lookup and node-level behavior.
- `server`: self-hosted ComfyUI server routes, messages, and execution behavior.
- `cloud`: Comfy Cloud APIs, jobs, files, workflows, and assets.
- `custom-node`: custom node install, debugging, migration, and authoring guidance.
- `registry`: registry publishing flow, versions, publishers, and install-resolution APIs.
- `install` / `troubleshoot`: installation, manager behavior, break-fix, and recovery.

## Snapshot Completeness Contract

Treat coverage as complete only when all conditions are true:

1. `references/sitemap.xml` exists.
2. `references/docs-manifest.tsv` exists and maps sitemap URLs.
3. `references/snapshot-metadata.json` reports `coverage_complete = true`.
4. `references/docs/` contains mapped markdown pages.
5. `python3 scripts/audit_snapshot.py` exits `0`.

## Freshness Rules

- Refresh first for "latest", "current", "new", API behavior changes, or Cloud questions.
- If refresh is not possible, answer from the current snapshot and state the snapshot date from `references/snapshot-metadata.json`.

## Recent Reliability Improvements

- **Atomic sync by default**: writes into a staging directory and swaps into live snapshot only after success.
- **Failure isolation**: failed sync does not corrupt live snapshot.
- **Structured swap errors**: atomic swap now emits stage-specific error categories.
- **Cleaner snippets**: search suppresses Mintlify index preamble noise lines.
- **Better relevance**: search now downweights stopwords/short noise terms and boosts title matches.
- **Task-aware search presets**: search can narrow to workflow, server, cloud, registry, and other doc families.
- **Curated routing guide**: `references/task-routing.md` gives agents a fast entrypoint for common ComfyUI tasks.

## Source Policy

- Official docs only (`docs.comfy.org`) unless explicitly requested otherwise.
- For behavior-critical answers, cite exact official page URLs from `docs-manifest.tsv`.
- Keep self-hosted server docs and Cloud docs separate.
- If the official docs do not confirm a field, route, or behavior, say so directly instead of guessing.
