# ContextL Engine: Technical Documentation

This document explains the inner workings of ContextL, a high-performance repository intelligence engine designed to feed precise context to AI coding agents.

## Architecture Overview

ContextL operates entirely locally without using LLMs or vector embeddings. It relies on a deterministic **4-Step Pipeline** that transforms raw source code into a mathematical graph of import relationships, which is then scored against natural language queries using a custom BM25 + PageRank algorithm.

### The 4-Step Pipeline

1. **Scan (`scanner.py`)**
   The engine recursively traverses the file system starting at the repository root. It filters out non-source files (like `.png`, `.pdf`) and ignored directories (like `node_modules`, `.git`, `__pycache__`). It collects the size, path, and extension of all valid source files.

2. **Parse (`import_parser.py`)**
   Every discovered source file is parsed to extract its outgoing imports. 
   - **Primary Engine:** ContextL uses `tree-sitter`, an incredibly fast, incremental C-based parsing library. It walks the Abstract Syntax Tree (AST) of 7 supported languages (Python, TypeScript, JavaScript, Java, Go, Rust, C/C++) to accurately resolve relative imports, aliases, and scoping.
   - **Fallback Engine:** If `tree-sitter` is unavailable on the host machine, the engine gracefully falls back to a highly optimized regex extraction engine.

3. **Graph (`graph_builder.py`)**
   The extracted import statements are resolved into absolute paths and fed into a directed graph using the `networkx` library.
   - **Nodes:** Every source file is a node.
   - **Edges:** Every import is a directed edge from the importer to the imported file.
   - **Metrics:** Once the graph is built, the engine calculates the in-degree (how often a file is imported) and out-degree for each node.
   - **PageRank:** The engine runs Google's classic PageRank algorithm across the graph to determine the overall "centrality" or importance of every file. Cycles (circular dependencies) are mathematically penalized to prevent score inflation.

4. **Query (`query_engine.py`)**
   When an AI agent searches for a feature (e.g., "auth middleware session"), the engine scores every file in the graph.
   - **TF-IDF & BM25:** The engine uses BM25 term frequency to score how often query terms appear in the file. BM25 prevents massive 10,000-line files from stealing top spots just because they have more words.
   - **Structural Multipliers:** If a query term matches a declared class name, method, or file name, it receives a massive multiplier (up to 10x). This makes the engine behave semantically even though it uses keyword matching.
   - **Neighbor Propagation:** Files that match a query pass a fraction of their score to their neighbors in the graph (both files they import and files that import them). This allows the engine to surface files that don't explicitly contain the query term, but are tightly coupled to files that do.

## Performance & Caching (`mcp_server.py`)

Building the graph takes ~50-300ms depending on repository size. To prevent this overhead on every single AI query, ContextL maintains a persistent in-memory graph cache during an active MCP session. 

When a query arrives, ContextL hashes the modification times (`mtime`) of all source files. If the hash hasn't changed, the query is executed against the cached graph in `< 1ms`. If a file has been modified (e.g., the user saved a file), the graph is rebuilt incrementally.

## Dependency Overview

ContextL was designed to be as lightweight as possible. It relies on three core dependencies:

1. **`networkx`**: Used in `graph_builder.py` and `impact_analysis.py`. This library provides the mathematical backbone for directed graphs, PageRank calculations, strongly connected component detection, and BFS/DFS graph traversals.
2. **`tree-sitter`**: Used in `import_parser.py`. This provides AST-level accuracy when resolving imports, preventing the engine from being fooled by comments or string literals that happen to contain the word "import".
3. **`mcp`**: The official Model Context Protocol SDK. Used in `mcp_server.py` to expose the engine's Python functions over `stdio` so that IDEs like Cursor and Windsurf can interact with it.
