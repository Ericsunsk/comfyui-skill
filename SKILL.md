---
name: comfyui-official-docs
description: "Official ComfyUI documentation skill backed by a local full snapshot of docs.comfy.org. Use when planning, building, debugging, or implementing ComfyUI workflows, workflow JSON, built-in node usage, self-hosted server integrations, Comfy Cloud API calls, custom node installation/development, registry publishing, manager behavior, or official troubleshooting. Use when the task needs exact node names, schema fields, endpoint paths, request/response details, or citation-backed latest official behavior."
---

# ComfyUI Official Docs

Use this skill when ComfyUI work should follow official docs, not community memory.

## What This Skill Covers

- Designing or fixing ComfyUI workflows with official nodes and templates.
- Editing or generating workflow JSON that must match the official schema.
- Implementing self-hosted ComfyUI server integrations.
- Implementing Comfy Cloud API integrations.
- Installing, debugging, developing, or publishing custom nodes with official guidance.
- Answering behavior-critical ComfyUI questions with exact citations.

## Source Of Truth

1. `references/docs/` is the local mirror of `docs.comfy.org`.
2. `references/docs-manifest.tsv` maps local files to exact official URLs.
3. `references/snapshot-metadata.json` records snapshot freshness and completeness.
4. `references/task-routing.md` is the fast path for common task families.

## Quick Start

1. Search the current snapshot by task first, not by a single broad query:
   - Workflow / JSON: `python3 scripts/search_official_docs.py "your query" --task workflow --top 10`
   - Built-in nodes: `python3 scripts/search_official_docs.py "KSampler" --task node --section built-in-nodes --top 5`
   - Self-hosted server: `python3 scripts/search_official_docs.py "queue prompt websocket routes" --task server --top 8`
   - Cloud API: `python3 scripts/search_official_docs.py "submit workflow execution" --task cloud --top 8`
   - Custom nodes: `python3 scripts/search_official_docs.py "missing custom node" --task custom-node --top 8`
   - Registry: `python3 scripts/search_official_docs.py "publish node version" --task registry --top 8`
2. Open the matched markdown files under `references/docs/`.
3. Cite the exact official URLs from `references/docs-manifest.tsv`.
4. Refresh the snapshot only when freshness matters or the snapshot is missing:
   - Full refresh: `python3 scripts/sync_official_docs.py --clean`
   - Incremental refresh: `python3 scripts/sync_official_docs.py`
5. Audit completeness when you refreshed or when coverage is uncertain:
   `python3 scripts/audit_snapshot.py`

## Task Routing

1. Workflow design or debugging:
   Start with `--task workflow`.
   Use a tutorial or `development/core-concepts/workflow.md` to establish structure.
   Validate exact node names and inputs against the matching `built-in-nodes/*.md` files.
   If you emit or edit JSON, validate against `specs/workflow_json.md`.
2. Built-in node lookup:
   Search the exact node name with `--task node --section built-in-nodes`.
   Prefer the exact node page over tutorial snippets.
3. Self-hosted server automation:
   Use `--task server`.
   Stay inside `development/comfyui-server/*` unless the user explicitly asks about Cloud.
4. Comfy Cloud:
   Use `--task cloud`.
   Open the exact `api-reference/cloud/...` page before citing payloads or responses.
5. Custom nodes and registry:
   Use `--task custom-node` for installation, missing-node, migration, or authoring issues.
   Use `--task registry` for publishing, versions, PATs, publishers, or install-resolution APIs.
6. Installation and troubleshooting:
   Use `--task install` or `--task troubleshoot`.
   Prefer `installation/*`, `manager/*`, and `troubleshooting/*` over generic search.

## Retrieval Rules

1. Reuse exact strings from the user whenever possible:
   node names, route names, schema fields, error text, workflow feature names.
2. For exact lookups or noisy search results, use:
   `rg -n "your exact token" references/docs references/llms-full.txt`
3. Search results are only the routing layer.
   Always open the matched page before answering schema, API, or behavior questions.
4. Distinguish citation-backed facts from your inference.
5. If official docs do not confirm a field, route, node behavior, or third-party custom-node detail, say so directly.
6. Treat model file names, local paths, checkpoint availability, and third-party node behavior as environment-specific unless the docs explicitly define them.

## Freshness And Coverage

1. For "latest", "new", "recent", "current", API behavior changes, or Cloud features, sync first.
2. Mention the snapshot date from `references/snapshot-metadata.json` when answering time-sensitive questions.
3. Treat coverage as complete only when:
   - `references/sitemap.xml` exists.
   - `references/docs-manifest.tsv` exists.
   - `references/snapshot-metadata.json` reports `coverage_complete = true`.
   - `python3 scripts/audit_snapshot.py` exits `0`.
4. If coverage is incomplete, rerun:
   `python3 scripts/sync_official_docs.py --clean --workers 8 --retries 5`
5. If network refresh is not possible, answer from the current snapshot and state the snapshot date explicitly.

## Reference Files

- `references/task-routing.md`: task-to-doc-family routing for common ComfyUI jobs.
- `references/sitemap.xml`: official page inventory.
- `references/llms.txt`: official docs index links.
- `references/llms-full.txt`: consolidated docs text for exact-string lookup fallback.
- `references/docs/`: per-page markdown mirror from official `.md` endpoints.
- `references/docs-manifest.tsv`: URL mapping and sync status.
- `references/snapshot-metadata.json`: sync metadata and last snapshot time.
- `references/coverage.md`: section counts and failed page list.
- `scripts/audit_snapshot.py`: strict completeness and integrity audit.

## Operating Rules

1. Prefer official docs.comfy.org content over memory.
2. Do not mix unofficial community guidance unless explicitly requested.
3. Keep local server guidance and Cloud guidance separate.
4. Report exact page URLs for endpoint-level, schema-level, and behavior-critical claims.
5. Mention the snapshot date when answering "latest" questions.
