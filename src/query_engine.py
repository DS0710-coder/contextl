"""
Repository Intelligence Engine
Step 4: Query Engine

Accepts a natural-language query and ranks files by relevance using:

  1. Keyword match score  — does the filename / path contain query terms?
  2. Content match score  — do the file's contents mention query terms?
  3. Graph neighbor bonus — if a high-scoring file is nearby in the graph,
                            its neighbors get a proximity boost
  4. Centrality weight    — more connected files rank slightly higher when
                            scores are otherwise equal

No LLM. No embeddings. Pure text + graph.
"""

import math
import re
from dataclasses import dataclass, field

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph, RepoGraph


# ---------------------------------------------------------------------------
# Stop words — stripped from queries before matching
# ---------------------------------------------------------------------------
STOP_WORDS = {
    "a", "an", "the", "in", "on", "at", "to", "for", "of", "and",
    "or", "is", "it", "this", "that", "with", "from", "how", "what",
    "where", "when", "which", "who", "make", "change", "update", "fix",
    "add", "remove", "edit", "modify", "the", "my", "our", "i", "we",
    "string", "int", "boolean", "class", "function", "return", "import",
    "public", "private", "logic", "handler", "data", "value"
}


@dataclass
class RankedFile:
    """A file with its relevance score and scoring breakdown."""
    path: str
    total_score: float
    keyword_score: float   # path/filename match
    content_score: float   # file content match
    neighbor_bonus: float  # proximity to other high-scoring files
    centrality: float      # PageRank weight
    matched_terms: list[str] = field(default_factory=list)

    def explain(self) -> str:
        terms = ", ".join(self.matched_terms) if self.matched_terms else "none"
        return (
            f"  {self.path}\n"
            f"    score={self.total_score:.4f}  "
            f"keyword={self.keyword_score:.3f}  "
            f"content={self.content_score:.3f}  "
            f"neighbor={self.neighbor_bonus:.3f}  "
            f"centrality={self.centrality:.4f}\n"
            f"    matched terms: {terms}"
        )


def _tokenize(text: str) -> list[str]:
    """Lowercase, split on non-alphanumeric, remove stop words."""
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def _path_tokens(path: str) -> list[str]:
    """Extract meaningful tokens from a file path."""
    # Split on slashes, dots, camelCase, kebab-case, underscores
    parts = re.split(r"[/\\.]", path)
    tokens = []
    for part in parts:
        # Split camelCase: LoginHeader → login, header
        sub = re.sub(r"([A-Z])", r" \1", part).lower()
        tokens.extend(re.findall(r"[a-z0-9]+", sub))
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def _keyword_score(query_terms: list[str], file_path: str, idf_weights: dict[str, float]) -> tuple[float, list[str]]:
    """
    Score how well query terms match the file path / name.
    Filename matches score higher than directory matches.
    """
    path_toks = _path_tokens(file_path)
    filename_toks = _path_tokens(file_path.split("/")[-1])

    matched = []
    score = 0.0

    for term in query_terms:
        if term in filename_toks:
            score += idf_weights.get(term, 1.0)   # Strong signal: term in filename
            matched.append(term)
        elif term in path_toks:
            score += 0.4 * idf_weights.get(term, 1.0)   # Weaker signal: term in directory path
            if term not in matched:
                matched.append(term)

    # Normalize by max possible score (sum of all IDFs)
    max_score = sum(idf_weights.get(t, 1.0) for t in query_terms)
    if max_score > 0:
        score = score / max_score

    return score, matched


def _content_score(query_terms: list[str], file_content: str, idf_weights: dict[str, float]) -> tuple[float, list[str]]:
    """
    Score how often query terms appear in the file's source code.
    Uses TF-IDF weighting, capped to avoid huge files dominating.
    """
    content_tokens = set(re.findall(r"[a-z0-9]+", file_content))
    matched = [t for t in query_terms if t in content_tokens]

    if not query_terms:
        return 0.0, []

    score = sum(idf_weights.get(t, 1.0) for t in matched)
    max_score = sum(idf_weights.get(t, 1.0) for t in query_terms)
    if max_score > 0:
        score = score / max_score
    else:
        score = 0.0

    return score, matched


def _apply_neighbor_bonus(
    scores: dict[str, float],
    repo_graph: RepoGraph,
    boost: float = 0.15,
    depth: int = 1,
) -> dict[str, float]:
    """
    Files neighbouring high-scoring files get a proximity boost.
    Runs one pass: find top scorers, boost their graph neighbors.
    """
    if not scores:
        return scores

    max_score = max(scores.values()) or 1.0
    boosted = dict(scores)

    for path, score in scores.items():
        # Only propagate from files with meaningful scores
        if score < 0.1:
            continue

        neighbors = repo_graph.get_neighbors(path, depth=depth)
        for neighbor in neighbors:
            if neighbor in boosted:
                # Boost proportional to how strong the source signal is
                boosted[neighbor] += boost * (score / max_score)

    return boosted


def query(
    q: str,
    repo_graph: RepoGraph,
    top_n: int = 10,
) -> list[RankedFile]:
    """
    Rank all files in the repository by relevance to a natural-language query.

    Args:
        q:          Natural-language query string.
        repo_graph: Built graph from build_graph().
        top_n:      Maximum number of results to return.

    Returns:
        List of RankedFile sorted by total_score descending.
    """
    query_terms = _tokenize(q)

    if not query_terms:
        return []

    # --- Pre-computation: Global TF-IDF ---
    total_files = len(repo_graph.nodes)
    document_frequency = {term: 0 for term in query_terms}
    
    file_contents = {}
    for path, node in repo_graph.nodes.items():
        abs_path = node.path if hasattr(node, "absolute_path") else str(__import__("pathlib").Path(repo_graph.root) / path)
        try:
            content = open(abs_path, encoding="utf-8").read().lower()
            file_contents[path] = content
            content_tokens = set(re.findall(r"[a-z0-9]+", content))
            path_tokens = set(_path_tokens(path))
            combined_tokens = content_tokens.union(path_tokens)
            for term in query_terms:
                if term in combined_tokens:
                    document_frequency[term] += 1
        except Exception:
            file_contents[path] = ""

    idf_weights = {}
    for term in query_terms:
        df = document_frequency[term]
        idf_weights[term] = math.log(total_files / (1 + df)) if total_files > 0 else 1.0

    # --- Pass 1: keyword + content scores per file ---
    keyword_scores: dict[str, float] = {}
    content_scores: dict[str, float] = {}
    matched_terms: dict[str, list[str]] = {}

    for path, node in repo_graph.nodes.items():
        kscore, kterms = _keyword_score(query_terms, path, idf_weights)
        cscore, cterms = _content_score(query_terms, file_contents.get(path, ""), idf_weights)

        keyword_scores[path] = kscore
        content_scores[path] = cscore
        matched_terms[path] = list(set(kterms + cterms))

    # --- Pass 2: combine into base score ---
    base_scores: dict[str, float] = {}
    for path in repo_graph.nodes:
        base_scores[path] = (
            keyword_scores.get(path, 0.0) * 0.5 +
            content_scores.get(path, 0.0) * 0.5
        )

    # --- Pass 3: neighbor bonus ---
    boosted_scores = _apply_neighbor_bonus(base_scores, repo_graph)

    # --- Pass 4: centrality tiebreaker ---
    results = []
    for path, node in repo_graph.nodes.items():
        neighbor_bonus = boosted_scores[path] - base_scores[path]
        total = boosted_scores[path] + node.centrality * 0.05

        results.append(RankedFile(
            path=path,
            total_score=total,
            keyword_score=keyword_scores.get(path, 0.0),
            content_score=content_scores.get(path, 0.0),
            neighbor_bonus=neighbor_bonus,
            centrality=node.centrality,
            matched_terms=matched_terms.get(path, []),
        ))

    # Sort by total score descending
    results.sort(key=lambda r: r.total_score, reverse=True)

    # Return only files with non-zero score, up to top_n
    return [r for r in results if r.total_score > 0.01][:top_n]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python query_engine.py <repo_path> '<query>'")
        print("Example: python query_engine.py ../Lazy-Footers 'change the download button'")
        sys.exit(1)

    target = sys.argv[1]
    user_query = sys.argv[2]

    print(f"Query: '{user_query}'")
    print(f"Repo:  {target}")
    print()

    scan = scan_repo(target)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    ranked = query(user_query, repo_graph)

    if not ranked:
        print("No relevant files found.")
    else:
        print(f"Top {len(ranked)} relevant files:\n")
        for i, result in enumerate(ranked, 1):
            print(f"{i}.")
            print(result.explain())
            print()
