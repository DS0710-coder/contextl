# contextl

**Architecture intelligence for AI coding agents.**

Stop letting your AI agent read your entire codebase to make one small change. `contextl` finds the exact files that matter — using graph theory, not guesswork.

```
"fix the broken checkout flow"
        ↓
components/Checkout.tsx      [high confidence]
lib/api.ts                   [high confidence]
types/index.ts                [medium confidence]
```

No LLM. No embeddings. No API keys. No vector database. Pure dependency graph + text scoring — runs entirely on your machine, your code never leaves your laptop.

---

## Install (60 seconds)

**Requires Python 3.9+** on your PATH. Everything else (`networkx`, `mcp`) installs automatically on first run.

### Option 1: The AI Prompt Method (Recommended)
Since you are using an AI IDE, you don't even need to edit the configuration yourself. Just open Cursor's Composer or Claude Code's chat and paste this prompt:

> *"Hey, add the `contextl` MCP server to your configuration file. The command is `npx` and the args are `["-y", "contextl"]`."*

The AI will find its own config file, inject the JSON, and reboot automatically.

### Option 2: The Manual Method
If you prefer to configure it manually, add this to your IDE's MCP config file:

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

**Where to find your config file:**

| IDE | Config path |
|-----|-------------|
| Antigravity | `~/.gemini/config/mcp_config.json` |
| Cursor | `~/.cursor/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Claude Code | `~/.claude.json` |
| VS Code | `.vscode/mcp.json` |

Restart your IDE. Done — no cloning, no Python setup beyond having it installed.

---

## What it gives your agent

Seven tools, automatically available once connected:

### `query_repo`
*"Find the files relevant to this change."*

Ranks every file in your repo against a natural-language query using filename matching, content matching, and graph proximity. Returns confidence-scored results with plain-English reasoning.

### `analyze_impact`
*"If I change this file, what breaks?"*

Walks the dependency graph upstream from any file to find every direct and transitive dependent. Flags likely test files so your agent knows what to re-run. Essential before touching shared files like `types/`, `utils/`, or config.

### `scan_repo`
*"What files exist here?"*

Lists every source file `contextl` can see — useful for the agent to orient itself before doing anything else.

### `find_dead_files`
*"Which files are never imported by anything?"*

Finds unused files and dead code by analyzing the dependency graph for files with an in-degree of 0. Automatically filters out standard entry points (like `page.tsx` or `index.ts`) and test files.

### `export_obsidian_vault`
*"Visualize this codebase in Obsidian."*

Takes the exact dependency graph built by the intelligence engine and physically writes it to disk as a directory of interconnected Markdown files. Automatically injects file metadata, JSDoc/Docstring explanations, and uses standard `[[wikilinks]]` to map out dependencies. Open the generated folder as an Obsidian vault for a stunning 3D interactive graph of your architecture!

### `review_changes`
*"I'm reviewing or changing some code. What's the impact?"*

Git-aware context builder. Reads the current git diff to find what files you are editing, then automatically runs impact analysis to find every file that depends on your changes. Returns a structured context bundle with the changed files, full blast radius, and suggested tests to re-run.

### `get_skeleton`
*"Show me the API of this huge file."*

Extracts the structural skeleton (API surface) of a source file using Tree-sitter — including all class names, method signatures, return types, and docstrings — without pulling in any implementation bodies. Shrinks a 5,000-line file into a ~100-line reference header.



## How the ranking works

1. **Keyword match** — does the filename contain query terms?
2. **Content match** — does the file's source code mention the terms?
3. **Graph proximity** — files connected to high-scoring files get a relevance boost
4. **Centrality (PageRank)** — heavily-connected files rank higher when scores tie

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
contextl impact ./my-repo src/api.ts

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

AI coding agents are increasingly good at writing code. They're still bad at knowing *where* to look. On a 5,000-file repo, an agent might read 100+ files just to change a logo. `contextl` exists to fix that — and to eventually give agents a real model of your codebase's architecture, not just a file list.

---

## Also available for Python

```bash
pip install contextl-mcp
```

Same engine, same tools — installable via PyPI for Python-first workflows.

---

## Links

- [Creator GitHub](https://github.com/DS0710-coder)
- [PyPI package](https://pypi.org/project/contextl-mcp)

## License

MIT
