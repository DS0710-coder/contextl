# contextl

> **Context-selection engine for AI coding assistants.**  
> Finds the most relevant files in your codebase for a natural-language change request — no LLM, no embeddings, no vector database. Pure graph + text scoring.

```
"fix the upload error" → [FileUploader.tsx, lib/upload.ts, UploadSection.tsx]
```

Instead of feeding your entire repo to an AI, `contextl` reduces 5 000 files down to the 5 most relevant ones in milliseconds.

---

## Quick start

**Requires Python 3.9+** on your PATH. Everything else (`networkx`, `mcp`) is installed automatically on first run.

### 1 — Add to your IDE's MCP config

Paste this JSON into your IDE's MCP config file (paths listed below):

```json
{
  "mcpServers": {
    "contextl": {
      "command": "npx",
      "args": ["-y", "contextl"]
    }
  }
}
```

#### Config file locations

| IDE | Config file |
|-----|-------------|
| **Antigravity** | `~/.gemini/antigravity/mcp/` (MCP server directory) |
| **Cursor** | `~/.cursor/mcp.json` |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` |
| **Claude Code** | `~/.claude.json` (or run `claude mcp add`) |
| **VS Code** | `.vscode/mcp.json` in your workspace root |

### 2 — Use it

Just talk to your IDE's AI normally:

```
You:  "fix the file upload error handler"
IDE:  calls query_repo → gets [FileUploader.tsx, lib/upload.ts, …]
IDE:  reads only those 5 files instead of the whole repo
```

---

## Tools exposed

### `query_repo(repo_path, query, top_n?)`

Ranks the most relevant files for a change request.

**Parameters:**
- `repo_path` — absolute path to the repository root
- `query` — natural-language description of the change (e.g. `"change the download button color"`)
- `top_n` — max results to return (default `5`, max `20`)

**Returns:**
```json
{
  "query": "change the download button",
  "repo": "/path/to/repo",
  "total_files_scanned": 142,
  "results": [
    {
      "rank": 1,
      "path": "components/DownloadButton.tsx",
      "score": 0.9800,
      "confidence": "high",
      "matched_terms": ["button", "download"],
      "reasoning": "Filename strongly matches query terms; file contents heavily reference query terms."
    }
  ]
}
```

### `scan_repo(repo_path)`

Lists all source files the engine can see in a repository. Useful for verifying coverage before querying.

**Returns:**
```json
{
  "repo": "/path/to/repo",
  "total_files": 142,
  "files": [
    { "path": "components/Button.tsx", "extension": ".tsx", "size_bytes": 1024 }
  ]
}
```

---

## How it works

The engine runs **entirely locally** — no network calls, no AI APIs, no data leaves your machine.

Scoring uses four signals:

| Signal | Weight | Description |
|--------|--------|-------------|
| Keyword match | 0.5 | Query terms in the file path / name |
| Content match | 0.5 | Query terms inside the file source |
| Neighbor bonus | +0.15 | Files near high-scoring files in the import graph |
| PageRank | 0.05 | Tiebreaker: more connected files rank slightly higher |

Supports **Next.js / React / TypeScript** repos (`.ts`, `.tsx`, `.js`, `.jsx`). Automatically detects `@/` path aliases from `tsconfig.json`.

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Node.js | ≥ 18 |
| Python | ≥ 3.9 |
| `networkx` | auto-installed |
| `mcp` | auto-installed |

---

## License

MIT
