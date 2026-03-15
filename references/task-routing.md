# ComfyUI Agent Task Routing

Use this file when the user asks you to build, debug, or integrate ComfyUI and you need a fast path into the official docs snapshot.

## Pick the right lane

| Need | Search command | Open first |
|---|---|---|
| Build or fix a workflow | `python3 scripts/search_official_docs.py "your query" --task workflow --top 8` | `development/core-concepts/workflow.md`, a matching `tutorials/*` page, then `specs/workflow_json.md` if you will emit JSON |
| Find an official built-in node | `python3 scripts/search_official_docs.py "KSampler" --task node --section built-in-nodes --top 5` | `built-in-nodes/<NodeName>.md` |
| Use the self-hosted ComfyUI server | `python3 scripts/search_official_docs.py "queue prompt websocket routes" --task server --top 8` | `development/comfyui-server/comms_overview.md`, `comms_routes.md`, `comms_messages.md` |
| Use Comfy Cloud APIs | `python3 scripts/search_official_docs.py "submit workflow execution" --task cloud --top 8` | `development/cloud/overview.md`, then the exact `api-reference/cloud/...` page |
| Install or debug custom nodes | `python3 scripts/search_official_docs.py "missing custom node security level" --task custom-node --top 8` | `installation/install_custom_node.md`, `manager/pack-management.md`, `troubleshooting/custom-node-issues.md` |
| Publish to the registry | `python3 scripts/search_official_docs.py "publish node version" --task registry --top 8` | `registry/publishing.md`, `registry/specifications.md`, then exact `api-reference/registry/...` pages |
| Install, update, or recover ComfyUI | `python3 scripts/search_official_docs.py "portable windows update pip" --task install --top 8` | Matching `installation/*`, `manager/*`, or `troubleshooting/*` page |

## Retrieval rules

1. Reuse exact strings from the user whenever possible: node names, route names, error text, schema fields, or product names.
2. Search gets you to the page; it does not replace opening the page. Always read the matched markdown before answering schema or API questions.
3. For workflow work, use this order:
   tutorial or workflow concept -> exact built-in node docs -> workflow JSON schema.
4. Keep self-hosted server docs and Cloud API docs separate:
   `development/comfyui-server/*` is local server behavior;
   `api-reference/cloud/*` is Comfy Cloud.
5. If the official docs do not confirm a field, route, or behavior, say that directly instead of inferring unsupported details.

## Exact lookup fallback

Use ripgrep when the user already gave you an exact token:

```bash
rg -n "KSampler|prompt_id|execution_error|security_level" references/docs references/llms-full.txt
```

Use `references/docs-manifest.tsv` to map a local markdown file back to the exact official URL you should cite.
