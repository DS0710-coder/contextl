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

## Install

```bash
pip install contextl-mcp
```

### Option 1: The AI Prompt Method (Recommended)
Since you are using an AI IDE, you don't even need to edit the configuration yourself. Just open Cursor's Composer or Claude Code's chat and paste this prompt:

> *"Hey, add the `contextl` MCP server to your configuration file. The command is `contextl`."*

The AI will find its own config file, inject the JSON, and reboot automatically.

### Option 2: The Manual Method
If you prefer to configure it manually, add this to your IDE's MCP config file:

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
| Cursor | `~/.cursor/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Claude Code | `~/.claude.json` |
| VS Code | `.vscode/mcp.json` |

Restart your IDE. The `contextl` command is now available — `pip install` registered it on your PATH.

---

## What it gives your agent

Three tools, automatically available once connected:

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

---

## How the ranking works

1. **Keyword match** — does the filename contain query terms?
2. **Content match** — does the file's source code mention the terms?
3. **Graph proximity** — files connected to high-scoring files get a relevance boost
4. **Centrality (PageRank)** — heavily-connected files rank higher when scores tie

No machine learning involved — every score is fully explainable and traceable back to a specific signal.

---

## Supported languages

TypeScript, TSX, JavaScript, JSX — built for Next.js and React codebases first.

Python, Go, and Rust support are on the roadmap.

---

## Why this exists

AI coding agents are increasingly good at writing code. They're still bad at knowing *where* to look. On a 5,000-file repo, an agent might read 100+ files just to change a logo. `contextl` exists to fix that — and to eventually give agents a real model of your codebase's architecture, not just a file list.

---

## Also available via npm

```bash
npx -y contextl
```

Same engine, same tools — installable via npm for JS/TS-first workflows.

---

## Links

- [GitHub](https://github.com/DS0710-coder/contextl)
- [npm package](https://npmjs.com/package/contextl)

## License

MIT
