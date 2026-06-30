# contextl-mcp

**Architecture intelligence for AI coding agents.**

Stop letting your AI agent read your entire codebase to make one small change. `contextl` finds the exact files that matter — using graph theory, not guesswork.

```
"fix the broken checkout flow"
        ↓
components/Checkout.tsx      [high confidence]
lib/api.ts                   [high confidence]
types/index.ts                [medium confidence]
```

No LLM. No embeddings. No API keys. No vector database. Pure dependency graph + text scoring — runs entirely on your machine, your code never leaves your system.

---

## Install (60 seconds)

**Requires Python 3.9+**. All required dependencies — graph processing and tree-sitter parsers for 7 languages — are automatically bundled via `pip`.

```bash
pip install contextl-mcp && contextl install
```

This will globally install the `contextl` CLI and automatically inject the correct configuration into your AI IDE (Cursor, Windsurf, Claude Code, etc.). 

Restart your IDE and the contextl tools will be instantly available to your agent!

### Manual Configuration (Fallback)
If the auto-installer doesn't detect your IDE, or if you prefer to configure it manually, add this to your IDE's MCP config file:

```json
{
  "mcpServers": {
    "contextl": {
      "command": "contextl"
    }
  }
}
```

**Where to find your config file:**

| IDE | Config path |
|-----|-------------|
| Antigravity | `~/.gemini/config/mcp_config.json` |
| Claude Desktop | `~/.config/Claude/claude_desktop_config.json` (varies by OS) |
| Cline / Roo | `~/Documents/Cline/cline_mcp_settings.json` (varies by OS) |
| Cursor | `~/.cursor/mcp.json` |
| Claude Code | `~/.claude.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| VS Code (Workspace) | `.vscode/mcp.json` |

Restart your IDE. The `contextl` command is now available — `pip install` registered it on your PATH.

---

## What it gives your agent

Seven tools, automatically available once connected:

### `query_repo`
*"Find the files relevant to this change."*

Ranks every file in your repo against a natural-language query using filename matching, content matching, and graph proximity. Returns confidence-scored results with plain-English reasoning.

```json
{
  "repo_path": "/path/to/repo",
  "query": "fix the upload error handler",
  "top_n": 5
}
```

### `analyze_impact`
*"If I change this file, what breaks?"*

Walks the dependency graph upstream from any file to find every direct and transitive dependent. Flags likely test files so your agent knows what to re-run. Essential before touching shared files like `types/`, `utils/`, or config.

```json
{
  "repo_path": "/path/to/repo",
  "target_file": "src/types/index.ts"
}
```

### `scan_repo`
*"What files exist here?"*

Lists every source file `contextl` can see — useful for the agent to orient itself before doing anything else.

### `find_dead_files`
*"Which files are never imported by anything?"*

Find files in the repository that are never imported by any other file (in-degree of 0 in the dependency graph). 

*Note: The engine automatically detects and excludes standard entry points (e.g. `src/index.ts`, `main.py`, `app.tsx`) and test files from these results, as they are intentionally not imported by other files.*

**Arguments:**

```json
{
  "repo_path": "/path/to/repo"
}
```

### `export_obsidian_vault`
*"Visualize this codebase in Obsidian."*

Takes the exact dependency graph built by the intelligence engine and physically writes it to disk as a directory of interconnected Markdown files. Automatically injects file metadata, JSDoc/Docstring explanations, and uses standard `[[wikilinks]]` to map out dependencies. Open the generated folder as an Obsidian vault for a stunning 3D interactive graph of your architecture!

```json
{
  "repo_path": "/path/to/repo",
  "output_dir": "/path/to/save/vault"
}
```

### `review_changes`
*"I'm reviewing or changing some code. What's the impact?"*

Git-aware context builder. Reads the current git diff to find what files you are editing, then automatically runs impact analysis to find every file that depends on your changes. Returns a structured context bundle with the changed files, full blast radius, and suggested tests to re-run.

```json
{
  "repo_path": "/path/to/repo",
  "staged": true,
  "unstaged": true
}
```

### `get_skeleton`
*"Show me the API of this huge file."*

Extracts the structural skeleton (API surface) of a source file using Tree-sitter — including all class names, method signatures, return types, and docstrings — without pulling in any implementation bodies. Shrinks a 5,000-line file into a ~100-line reference header.

```json
{
  "file_path": "/path/to/src/api.py"
}
```

---

## Benchmarks & Token Reduction

Instead of dumping an entire repository into your agent's context window, `contextl` surgically extracts only the relevant dependencies. Across 9 real-world open source repositories, this results in massive token savings while maintaining high relationship accuracy:

- **JavaScript (Express)**: 93.58% context reduction
- **C++ (JSON)**: 84.31% context reduction
- **Python (Flask)**: 52.69% context reduction

See the full live telemetry and methodology breakdown at our [official documentation and metrics dashboard](https://contextl-web.vercel.app).



## How the ranking works

`contextl` relies strictly on deterministic mathematical scoring based on Okapi BM25 and graph theory. There are no LLMs or embeddings involved.

1. **Keyword Match (Path / Filename)**
   - Exact filename matches receive a massive `4.0x` IDF multiplier.
   - Exact path matches receive a `2.0x` IDF multiplier.
   - Substring and canonical abbreviation matches (e.g., `db` matching `database.py`) also receive significant boosts.
2. **Content Match (BM25 TF-IDF & Structural Analysis)**
   - Calculates Okapi BM25 Term Frequency (`k1=1.5`, `b=0.75`), using Document Length Normalization to aggressively penalize huge files (e.g., 5,000-line god classes) and normalize token counts.
   - **TypeScript Exports**: Matches on `export const / class / function` receive a permanent `8.0x` multiplier.
   - **Classes / Interfaces**: Matches on OOP class definitions receive up to a `10.0x` structural multiplier for short vibe queries.
   - **Functions / Annotations**: Matches on method signatures and annotations receive a `4.0x` or `5.0x` boost.
3. **Graph Proximity Bonus**
   - Files directly adjacent in the dependency graph to high-scoring files receive a `0.2x` recursive relevance boost, pulling tightly coupled dependencies up the ranking.
4. **Centrality Tiebreaker**
   - The engine calculates PageRank across the entire repository graph. When files have identical or highly similar relevance scores, highly-central files heavily depended on by the rest of the codebase (like core `utils.py` or base classes) rank slightly higher.

*(Note: Test files are automatically penalized by 50% unless the natural language query explicitly contains words like "test" or "spec".)*

No machine learning involved — every score is fully explainable and traceable back to a specific signal.

---

## Supported languages

**JavaScript ecosystem**: TypeScript, TSX, JavaScript, JSX.
**Backend ecosystem**: Python (`.py`), Java (`.java`), Rust (`.rs`), Go (`.go`), C/C++ (`.cpp`, `.c`, `.h`).

The engine natively understands dot-notation module paths (`from X import Y`, `import com.example.X;`) and correctly resolves them to physical file paths to build the architecture graph.

> **Note:** Wildcard imports (e.g. `use super::*`, `use crate::*`) are intentionally left unresolved. ContextL maps explicit dependency paths only.

---

## The Global CLI

`contextl` isn't just an AI tool; it installs a global command-line interface on your system so you can access all the intelligence features natively:

```bash
# 1. Search the codebase
contextl search ./my-repo "fix the auth flow"

# 2. Analyze impact of changing a file
contextl impact ./my-repo src/api.py

# 3. Find dead unused files
contextl dead-code ./my-repo

# 4. Generate an Obsidian vault
contextl obsidian ./my-repo ./my_vault

# 5. Git-aware review / impact of current edits
contextl review ./my-repo
```

*(Note: If you omit the sub-command, `contextl ./my-repo "query"` will automatically default to `search` for backwards compatibility).*

---

## Why this exists

AI coding agents are increasingly good at writing code. They're still bad at knowing *where* to look. On a massive monorepo, an agent might blindly read 100+ files just to change a logo. `contextl` exists to fix that by giving agents a deterministic, graph-based map of your architecture.

And it scales. We rigorously benchmark against massive open source repositories to ensure it can handle your monorepo. On `typeorm` (3,572 TypeScript files), the engine scans, parses, graphs, and searches the entire architecture in under 3 seconds. On Apache `superset` (5,897 mixed language files), the full end-to-end pipeline executes in ~44 seconds. No vector DBs, no cloud latency, just pure on-device intelligence.

---

## Also available via npm

```bash
npx -y contextl
```

Same engine, same tools — installable via npm for JS/TS-first workflows.

---

## Links

- [Official Documentation & Benchmarks](https://contextl-web.vercel.app)
- [Creator GitHub](https://github.com/DS0710-coder)
- [npm package](https://npmjs.com/package/contextl)

## License

MIT
