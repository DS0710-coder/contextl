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

### `find_dead_files`
*"Which files are never imported by anything?"*

Finds unused files and dead code by analyzing the dependency graph for files with an in-degree of 0. Automatically filters out standard entry points (like `page.tsx` or `index.ts`) and test files.

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

---

## AI System Prompt (Query Optimizer)

ContextL is a deterministic keyword and graph engine, not a semantic AI. For maximum accuracy, inject this system prompt into your AI agent's rules (e.g., `.cursorrules` or custom instructions). It forces the AI to translate your natural language questions into highly optimized, lexical keyword strings before hitting the `query_repo` tool.

```text
System Instruction: You are a translation layer designed to convert human requests into highly optimized queries for the contextl codebase search engine. The contextl engine is NOT a semantic AI; it is an advanced, dependency-aware fuzzy keyword searcher. It relies on exact token matching and import-graph ranking.

Your goal is to extract the core technical keywords from the user's request and discard all conversational filler or vague concepts.

Rules for generating the query string:

1. Remove Conversational Filler: Drop words like "where is", "how does", "find the", "show me".
2. Translate Concepts to Code: If the user asks for a concept, translate it into the exact keywords, classes, or library syntax a developer would type.
Example: "routing" ➡️ createRouter Route routeTree
Example: "entry point" ➡️ main SpringBootApplication bootstrap web.xml init
Example: "database schema" ➡️ Entity Column Table model schema
3. Include Known Framework Terms: If you know the language or framework of the codebase, append its standard terminology.
4. Target File Types/Structures: If looking for configurations, use terms like config properties yaml xml json.
5. Keep it space-separated: Output a single string of space-separated keywords without punctuation.

Examples:

User: "Where are the main react components and routing defined?" 
Optimized Query: createRouter Route routeTree components layout

User: "Find the application entry point and main method." 
Optimized Query: public static void main bootstrap init ApplicationContext configuration

User: "How is the user authentication handled?" 
Optimized Query: login auth authenticate jwt token session passport

Input: [Insert human request here] 
Output: [Return ONLY the optimized keyword string]
```

---

## How the ranking works

1. **Keyword match** — does the filename contain query terms?
2. **Content match** — does the file's source code mention the terms?
3. **Graph proximity** — files connected to high-scoring files get a relevance boost
4. **Centrality (PageRank)** — heavily-connected files rank higher when scores tie

No machine learning involved — every score is fully explainable and traceable back to a specific signal.

---

## Supported languages

**JavaScript ecosystem**: TypeScript, TSX, JavaScript, JSX.
**Backend ecosystem**: Python (`.py`) and Java (`.java`).

The engine natively understands dot-notation module paths (`from X import Y`, `import com.example.X;`) and correctly resolves them to physical file paths to build the architecture graph.

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
```

*(Note: If you omit the sub-command, `contextl ./my-repo "query"` will automatically default to `search` for backwards compatibility).*

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

- [Creator GitHub](https://github.com/DS0710-coder)
- [npm package](https://npmjs.com/package/contextl)

## License

MIT
