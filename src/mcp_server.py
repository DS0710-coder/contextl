"""
Repository Intelligence Engine — Universal MCP Server

Exposes the engine as an MCP (Model Context Protocol) server over stdio.
Works with any MCP-compatible IDE: Cursor, Windsurf, Claude Code, VS Code, etc.

The IDE launches this script automatically when it needs it.
No manual server to keep running.

Usage (the IDE does this for you, but you can test manually):
    python mcp_server.py

Tools exposed:
    query_repo             — rank files by relevance to a natural-language query
    scan_repo              — list all source files the engine can see in a repo
    analyze_impact         — find every file affected by changing a target file
    find_dead_files        — find unimported files with in-degree 0
    export_obsidian_vault  — export repo graph to an Obsidian markdown vault

Performance:
    A shared graph cache is maintained per repo path + file mtime fingerprint.
    The 4-step build pipeline (scan → parse → graph → query) runs ONCE per
    session and is reused by all tool calls. Subsequent calls on an unchanged
    repo return from cache in <1ms.
"""

import asyncio
import json
import os
import sys
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Make sure the engine modules are importable from the same directory
sys.path.insert(0, str(Path(__file__).parent))

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query as engine_query
from main import _confidence, _reasoning
from impact_analysis import analyze_impact
from standalone import find_standalone_files
from obsidian_export import export_obsidian_vault
from git_review import _is_git_repo, get_changed_files, build_review_context, format_review_json
from import_parser import extract_skeleton


# ---------------------------------------------------------------------------
# Shared graph cache — one pipeline build per repo per session
# ---------------------------------------------------------------------------
@dataclass
class _CacheEntry:
    repo_path: str          # resolved absolute path
    mtime_hash: tuple[float, int]       # max mtime across all source files at build time, and total file count
    scan: object            # ScanResult
    repo_graph: object      # RepoGraph
    last_checked_time: float = 0.0


_cache_lock = threading.Lock()
_cache: dict[str, _CacheEntry] = {}


def _compute_mtime_hash(repo_path: str) -> tuple[float, int]:
    """Walk repo_path and return (maximum file modification time, file count)."""
    max_mtime = 0.0
    file_count = 0
    for dirpath, _, filenames in os.walk(repo_path):
        # Skip hidden dirs and common noise dirs
        dirpath_obj = Path(dirpath)
        if any(part.startswith(".") or part in ("node_modules", "__pycache__", ".git", "dist", "build", "target")
               for part in dirpath_obj.parts):
            continue
        for fname in filenames:
            try:
                mtime = os.path.getmtime(os.path.join(dirpath, fname))
                if mtime > max_mtime:
                    max_mtime = mtime
                file_count += 1
            except OSError:
                pass
    return (max_mtime, file_count)


def _get_graph(repo_path: str):
    """
    Return (scan, repo_graph) for the given repo_path.

    On first call (or after any source file changes): runs the full
    4-step pipeline and stores the result in the module-level cache.
    On subsequent calls with unchanged files: returns instantly from cache.
    """
    global _cache
    import time

    resolved = str(Path(repo_path).resolve())

    with _cache_lock:
        now = time.time()
        entry = _cache.get(resolved)
        
        # Fast path: bypass filesystem walk if checked within last 5 seconds.
        # This intentionally creates a 5s "blind window" where new/deleted/modified
        # files are not instantly detected, drastically reducing disk I/O on large repos
        # when the MCP client rapid-fires multiple queries concurrently.
        if entry and (now - entry.last_checked_time < 5.0):
            return entry.scan, entry.repo_graph

        mtime_hash = _compute_mtime_hash(resolved)

        if entry and entry.mtime_hash == mtime_hash:
            entry.last_checked_time = now
            print("[contextl] graph cache hit", file=sys.stderr, flush=True)
            return entry.scan, entry.repo_graph

        # Cache miss — build the pipeline
        print("[contextl] building graph...", file=sys.stderr, flush=True)
        scan = scan_repo(resolved)
        parse = parse_imports(scan)
        repo_graph = build_graph(scan, parse)

        _cache[resolved] = _CacheEntry(
            repo_path=resolved,
            mtime_hash=mtime_hash,
            scan=scan,
            repo_graph=repo_graph,
            last_checked_time=now,
        )
        print(f"[contextl] graph built: {scan.total_files} files", file=sys.stderr, flush=True)
        return scan, repo_graph


# ---------------------------------------------------------------------------
# Server setup
# ---------------------------------------------------------------------------
server = Server("repo-intelligence")


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="query_repo",
            description=(
                "Find the most relevant files in a code repository for a given "
                "change request or natural-language query. "
                "Returns a ranked list of files with relevance scores, confidence "
                "levels, matched terms, and a one-line reasoning string. "
                "Use this before editing code to identify exactly which files need "
                "to change — avoids reading irrelevant files."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "query": {
                        "type": "string",
                        "description": (
                            "SYSTEM INSTRUCTION: The contextl search engine is highly optimized for both raw conversational queries AND exact keyword searches. "
                            "It uses dynamic structural multipliers to instantly rank classes for short/conversational queries, and switches to BM25 frequency math for longer keyword queries.\n\n"
                            "STRATEGY INSTRUCTION:\n"
                            "1. INITIAL SEARCHES: Pass the user's raw natural-language query directly. Do NOT convert it to keywords. The engine is smart enough to drop stop-words and find the primary class anchors. Example: 'where is the auth logic?' -> 'where is the auth logic?'\n"
                            "2. TARGETED DEBUG SEARCHES: If the initial search fails, or if you are deep into debugging and need to cross-reference very specific variables across the codebase, then convert the query into highly optimized, space-separated keywords. Example: 'auth failure bug' -> 'login jwt AuthController retry_count token'\n"
                            "Never append generic filler words to targeted searches."
                        ),
                    },
                    "top_n": {
                        "type": "integer",
                        "description": "Maximum number of files to return (default: 5, max: 20).",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 20,
                    },
                },
                "required": ["repo_path", "query"],
            },
        ),
        types.Tool(
            name="scan_repo",
            description=(
                "Scan a repository and list all source files the engine can see. "
                "Useful for understanding the repository structure before querying. "
                "Returns file paths, extensions, and sizes."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                },
                "required": ["repo_path"],
            },
        ),
        types.Tool(
            name="analyze_impact",
            description=(
                "Find every file affected by changing a specific file. "
                "Walks the dependency graph upstream to find direct and transitive "
                "dependents — files that import the target file, and files that import "
                "those files. Flags likely test files so you know what to re-test. "
                "Use this BEFORE modifying a shared file (types, utils, config) to "
                "understand the blast radius of the change."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "target_file": {
                        "type": "string",
                        "description": (
                            "Path of the file being changed, relative to repo_path. "
                            "Example: 'src/types/index.ts' or 'lib/api.ts'. "
                            "Use scan_repo first if unsure of the exact path."
                        ),
                    },
                    "max_depth": {
                        "type": "integer",
                        "description": "Maximum hops to traverse upstream (default: 5).",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 10,
                    },
                },
                "required": ["repo_path", "target_file"],
            },
        ),
        types.Tool(
            name="find_dead_files",
            description=(
                "Find files in the repository that are never imported by any other file "
                "(in-degree of 0 in the dependency graph). Automatically filters out "
                "standard entry points and test files. Use this to identify standalone code "
                "and unused files that can potentially be deleted."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                },
                "required": ["repo_path"],
            },
        ),
        types.Tool(
            name="export_obsidian_vault",
            description=(
                "Generates an Obsidian Vault from the repository graph. "
                "Creates a folder of interconnected Markdown files using wikilinks "
                "so the codebase can be visualized in Obsidian's 3D graph view."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Absolute path to a folder where the vault should be created.",
                    },
                },
                "required": ["repo_path", "output_dir"],
            },
        ),
        types.Tool(
            name="review_changes",
            description=(
                "Git-aware context builder. Reads the current git diff (staged and/or "
                "unstaged) to find what files you are editing, then automatically runs "
                "impact analysis on each changed file to find every file that depends on "
                "your changes. Returns a structured context bundle containing: the changed "
                "files, their full blast radius (direct + transitive dependents), and a "
                "list of test files that should be re-run. Use this at the START of any "
                "code review or refactor session to instantly understand the full scope "
                "of your changes before touching anything."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the git repository root.",
                    },
                    "staged": {
                        "type": "boolean",
                        "description": "Include staged changes (git diff --cached). Default true.",
                        "default": True,
                    },
                    "unstaged": {
                        "type": "boolean",
                        "description": "Include unstaged working-tree changes (git diff). Default true.",
                        "default": True,
                    },
                },
                "required": ["repo_path"],
            },
        ),
        types.Tool(
            name="get_skeleton",
            description=(
                "Extract the structural skeleton (API surface) of a source file — all "
                "class names, method signatures, function signatures, return types, and "
                "docstrings — without any implementation bodies. "
                "Use this when you need to understand a file's API without consuming its "
                "full token count. A 5,000-line file becomes a ~100-line reference header. "
                "Supports: Python, TypeScript, JavaScript, TSX, JSX, Java, Rust."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Absolute path to the source file to extract the skeleton from.",
                    },
                },
                "required": ["file_path"],
            },
        ),
    ]


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:

    if name == "query_repo":
        return await _handle_query(arguments)

    if name == "scan_repo":
        return await _handle_scan(arguments)

    if name == "analyze_impact":
        return await _handle_impact(arguments)

    if name == "find_dead_files":
        return await _handle_dead_files(arguments)

    if name == "export_obsidian_vault":
        return await _handle_export_obsidian(arguments)

    if name == "review_changes":
        return await _handle_review_changes(arguments)

    if name == "get_skeleton":
        return await _handle_get_skeleton(arguments)

    return [types.TextContent(
        type="text",
        text=json.dumps({"error": f"Unknown tool: {name}"}),
    )]


async def _handle_query(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    query_str = args.get("query", "")
    top_n = min(int(args.get("top_n", 5)), 20)

    try:
        result = await asyncio.to_thread(_run_query, repo_path, query_str, top_n)
    except Exception as e:
        result = {"error": str(e), "query": query_str, "repo": repo_path, "results": []}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_query(repo_path: str, query_str: str, top_n: int) -> dict:
    """Uses cached graph — pipeline runs only on first call or after file changes."""
    scan, repo_graph = _get_graph(repo_path)
    ranked = engine_query(query_str, repo_graph, top_n=top_n)

    return {
        "query": query_str,
        "repo": scan.root,
        "total_files_scanned": scan.total_files,
        "results": [
            {
                "rank": i + 1,
                "path": r.path,
                "score": round(r.total_score, 4),
                "confidence": _confidence(r.total_score),
                "matched_terms": sorted(r.matched_terms),
                "reasoning": _reasoning(r, repo_graph),
            }
            for i, r in enumerate(ranked)
        ],
    }


async def _handle_scan(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")

    try:
        result = await asyncio.to_thread(_run_scan, repo_path)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_scan(repo_path: str) -> dict:
    """Uses cached graph — pipeline runs only on first call or after file changes."""
    scan, _ = _get_graph(repo_path)
    return {
        "repo": scan.root,
        "total_files": scan.total_files,
        "files": [
            {"path": f.path, "extension": f.extension, "size_bytes": f.size_bytes}
            for f in scan.files
        ],
    }


async def _handle_impact(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    target_file = args.get("target_file", "")
    max_depth = min(int(args.get("max_depth", 5)), 10)

    try:
        result = await asyncio.to_thread(_run_impact, repo_path, target_file, max_depth)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path, "target_file": target_file}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_impact(repo_path: str, target_file: str, max_depth: int) -> dict:
    """Uses cached graph — pipeline runs only on first call or after file changes."""
    scan, repo_graph = _get_graph(repo_path)
    report = analyze_impact(target_file, repo_graph, max_depth=max_depth)

    return {
        "target_file": report.target,
        "total_affected": report.total_affected,
        "directly_affected": [
            {"path": f.path, "is_test_file": f.is_test_file}
            for f in report.directly_affected
        ],
        "transitively_affected": [
            {
                "path": f.path,
                "distance": f.distance,
                "via": f.via,
                "is_test_file": f.is_test_file,
            }
            for f in report.transitively_affected
        ],
        "suggested_tests": report.test_files,
        "dependency_tree": report.to_tree_string(),
    }


async def _handle_dead_files(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")

    try:
        result = await asyncio.to_thread(_run_dead_files, repo_path)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_dead_files(repo_path: str) -> dict:
    """Uses cached graph — pipeline runs only on first call or after file changes."""
    scan, repo_graph = _get_graph(repo_path)
    standalone_files = find_standalone_files(repo_graph)

    return {
        "repo": scan.root,
        "total_files_scanned": scan.total_files,
        "total_standalone_files": len(standalone_files),
        "standalone_files": standalone_files
    }


async def _handle_export_obsidian(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    output_dir = args.get("output_dir", "")

    try:
        result = await asyncio.to_thread(_run_export_obsidian, repo_path, output_dir)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path, "output_dir": output_dir}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_export_obsidian(repo_path: str, output_dir: str) -> dict:
    """Uses cached graph — pipeline runs only on first call or after file changes."""
    scan, repo_graph = _get_graph(repo_path)
    vault_path = export_obsidian_vault(repo_path, output_dir)

    return {
        "repo": scan.root,
        "vault_path": vault_path,
        "total_files_exported": scan.total_files,
        "success": True
    }


async def _handle_review_changes(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    include_staged   = bool(args.get("staged", True))
    include_unstaged = bool(args.get("unstaged", True))

    try:
        result = await asyncio.to_thread(
            _run_review_changes, repo_path, include_staged, include_unstaged
        )
    except Exception as e:
        result = {"error": str(e), "repo": repo_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_review_changes(repo_path: str, include_staged: bool, include_unstaged: bool) -> dict:
    """Uses cached graph — builds review context from current git diff."""
    import json as _json

    if not _is_git_repo(repo_path):
        return {"error": f"'{repo_path}' is not a git repository."}

    staged, unstaged = get_changed_files(repo_path, include_staged, include_unstaged)

    if not staged and not unstaged:
        return {
            "repo": repo_path,
            "message": "No changed files found.",
            "changed_files": [],
            "all_affected": [],
            "suggested_tests": [],
        }

    _, repo_graph = _get_graph(repo_path)
    ctx = build_review_context(repo_path, staged, unstaged, repo_graph)
    return _json.loads(format_review_json(ctx))


async def _handle_get_skeleton(args: dict) -> list[types.TextContent]:
    file_path = args.get("file_path", "")

    try:
        result = await asyncio.to_thread(extract_skeleton, file_path)
    except Exception as e:
        result = {"error": str(e), "file": file_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Fallback for CLI users: route all arguments to the main.py CLI engine
        from main import main as cli_main
        try:
            cli_main()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        asyncio.run(main())
