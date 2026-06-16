"""
Repository Intelligence Engine
FastAPI REST Wrapper

Exposes the engine as a local HTTP API so agent IDEs and coding assistants
can call it programmatically.

Start server:
    uvicorn api:app --reload --port 8000

Endpoints:
    POST /query          — rank files by relevance
    GET  /health         — liveness check
    GET  /scan           — list all discovered files in a repo
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph, RepoGraph
from query_engine import query as engine_query, RankedFile
from main import _confidence, _reasoning, run_engine


# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Repository Intelligence Engine",
    description=(
        "Identifies the most relevant files in a codebase for a given "
        "natural-language query. No LLM, no embeddings — pure graph + text scoring."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------
class QueryRequest(BaseModel):
    repo_path: str = Field(..., description="Absolute or relative path to the repository root")
    query: str = Field(..., description="Natural-language query (e.g. 'fix the upload error handler')")
    top_n: int = Field(default=5, ge=1, le=50, description="Max results to return")


class FileResult(BaseModel):
    rank: int
    path: str
    score: float
    confidence: str          # "high" | "medium" | "low"
    matched_terms: list[str]
    reasoning: str


class QueryResponse(BaseModel):
    query: str
    repo: str
    elapsed_seconds: float
    results: list[FileResult]


class ScanRequest(BaseModel):
    repo_path: str = Field(..., description="Path to the repository root")


class ScanResponse(BaseModel):
    repo: str
    total_files: int
    files: list[dict]


class HealthResponse(BaseModel):
    status: str
    version: str


# ---------------------------------------------------------------------------
# Helper: build response items
# ---------------------------------------------------------------------------
def _build_results(ranked: list[RankedFile], repo_graph: RepoGraph) -> list[FileResult]:
    return [
        FileResult(
            rank=i + 1,
            path=r.path,
            score=round(r.total_score, 4),
            confidence=_confidence(r.total_score),
            matched_terms=sorted(r.matched_terms),
            reasoning=_reasoning(r, repo_graph),
        )
        for i, r in enumerate(ranked)
    ]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/health", response_model=HealthResponse, tags=["Meta"])
def health():
    """Liveness check — confirm the API is running."""
    return HealthResponse(status="ok", version="1.0.0")


@app.post("/query", response_model=QueryResponse, tags=["Engine"])
def query_files(req: QueryRequest):
    """
    Rank the most relevant files in a repository for a given change request.

    Returns up to `top_n` files ordered by relevance score, each annotated
    with a confidence level, matched terms, and a one-line reasoning string.
    """
    t0 = time.perf_counter()

    try:
        scan = scan_repo(req.repo_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if scan.total_files == 0:
        return QueryResponse(
            query=req.query,
            repo=scan.root,
            elapsed_seconds=round(time.perf_counter() - t0, 3),
            results=[],
        )

    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    ranked = engine_query(req.query, repo_graph, top_n=req.top_n)

    elapsed = round(time.perf_counter() - t0, 3)
    return QueryResponse(
        query=req.query,
        repo=scan.root,
        elapsed_seconds=elapsed,
        results=_build_results(ranked, repo_graph),
    )


@app.post("/scan", response_model=ScanResponse, tags=["Engine"])
def scan_files(req: ScanRequest):
    """
    Scan a repository and return a list of all discovered source files.
    Useful for previewing what the engine can see before running a query.
    """
    try:
        scan = scan_repo(req.repo_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return ScanResponse(
        repo=scan.root,
        total_files=scan.total_files,
        files=[
            {
                "path": f.path,
                "extension": f.extension,
                "size_bytes": f.size_bytes,
            }
            for f in scan.files
        ],
    )


# ---------------------------------------------------------------------------
# Dev server entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
