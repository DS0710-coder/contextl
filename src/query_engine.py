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
from impact_analysis import _is_test_file

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
    "public", "private", "logic", "handler", "data", "value", "yo", "bro",
    "bruh", "pls", "please", "bug", "issue", "error", "help", "stuff",
    "handling", "failing", "why", "need", "can", "could", "would", "should", "fr"
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
    """Lowercase, split on non-alphanumeric, remove stop words, deduplicate."""
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    # Deduplicate while preserving order
    return list(dict.fromkeys(t for t in tokens if t not in STOP_WORDS and len(t) > 1))


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

COMMON_ABBREVS = {
    "db": "database",
    "auth": "authentication",
    "config": "configuration",
    "pkg": "package",
    "app": "application",
    "svc": "service",
    "repo": "repository",
    "mgr": "manager",
    "impl": "implementation",
    "dir": "directory",
    "req": "request",
    "res": "response",
    "env": "environment",
    "src": "source",
    "lib": "library",
    "bin": "binary",
    "init": "initialize",
    "util": "utility",
    "utils": "utilities",
    "msg": "message",
    "err": "error",
    "ctx": "context",
    "fn": "function",
    "cmd": "command",
    "ctrl": "controller",
    "mid": "middleware"
}

REVERSE_ABBREVS = {v: k for k, v in COMMON_ABBREVS.items()}

def _is_match(term: str, target: str) -> bool:
    term_canon = COMMON_ABBREVS.get(term, term)
    if term_canon in target or target in term_canon or target.startswith(term_canon) or term_canon.startswith(target):
        return True
    if target == REVERSE_ABBREVS.get(term_canon):
        return True
    return False


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
        # Exact match on filename
        if term in filename_toks:
            score += 4.0 * idf_weights.get(term, 1.0)   # Massive signal
            matched.append(term)
        # Substring or abbreviation match on filename
        elif len(term) >= 2 and any(_is_match(term, ft) for ft in filename_toks):
            score += 3.0 * idf_weights.get(term, 1.0)
            matched.append(term)
        # Exact match on path
        elif term in path_toks:
            score += 2.0 * idf_weights.get(term, 1.0)   # Strong signal
            if term not in matched:
                matched.append(term)
        # Substring or abbreviation match on path
        elif len(term) >= 2 and any(_is_match(term, pt) for pt in path_toks):
            score += 1.5 * idf_weights.get(term, 1.0)
            if term not in matched:
                matched.append(term)

    # Normalize by max possible score (sum of all IDFs)
    max_score = sum(idf_weights.get(t, 1.0) for t in query_terms)
    if max_score > 0:
        base_normalized = min(1.0, sum(idf_weights.get(t, 1.0) for t in matched) / max_score)
        bonus = score - sum(idf_weights.get(t, 1.0) for t in matched)
        score = base_normalized + max(0, bonus)

    return score, matched


def _content_score(query_terms: list[str], file_path: str, file_content: str, idf_weights: dict[str, float], dl: int, avgdl: float) -> tuple[float, list[str]]:
    """
    Score how often query terms appear in the file's source code.
    Uses BM25 Term Frequency weighting to neutralize document length bias.
    Includes language-specific heuristics for Java and other OOP languages.
    """
    is_java = file_path.endswith(".java")
    is_ts = file_path.endswith(".ts") or file_path.endswith(".tsx")
    is_oop = is_java or is_ts
    
    content_tokens_list = re.findall(r"[a-z0-9]+", file_content.lower())
    
    # 1. CamelCase Splitting (Java only)
    if is_java:
        camel_tokens = []
        for word in re.findall(r"[a-zA-Z]+", file_content):
            if any(c.isupper() for c in word):
                sub = re.sub(r"([A-Z])", r" \1", word).lower()
                camel_tokens.extend(re.findall(r"[a-z0-9]+", sub))
        content_tokens_list.extend([t for t in camel_tokens if len(t) > 1])

    # 2. Extract Class Declarations, Annotations & Method Names
    declared_classes = set()
    ts_exports = set()
    java_methods = set()
    if is_oop or file_path.endswith(".py"):
        decls = re.findall(r"\b(?:class|interface|enum)\s+([a-zA-Z0-9_]+)", file_content)
        for d in decls:
            declared_classes.add(d.lower())
            
    if is_java:
        # Extract Java method names: public/private/protected ... methodName(
        methods = re.findall(r"\b(?:public|private|protected)\s+(?:static\s+)?(?:[a-zA-Z0-9_<>\[\]]+)\s+([a-zA-Z0-9_]+)\s*\(", file_content)
        for m in methods:
            if m.lower() not in {"main", "get", "set", "is", "has"}:
                java_methods.add(m.lower())
                # Also add CamelCase parts of method names
                sub = re.sub(r"([A-Z])", r" \1", m).lower()
                for part in re.findall(r"[a-z0-9]+", sub):
                    if len(part) > 3:
                        java_methods.add(part)
                        
    py_defs = set()
    if file_path.endswith(".py"):
        defs = re.findall(r"\b(?:def|async def)\s+([a-zA-Z0-9_]+)\s*\(", file_content)
        for d in defs:
            if d.lower() not in {"main", "init", "get", "set"}:
                py_defs.add(d.lower())
            
    if is_ts:
        exports = re.findall(r"\bexport\s+(?:const|let|var|class|interface|function|default)\s+([a-zA-Z0-9_]+)", file_content)
        for e in exports:
            ts_exports.add(e.lower())

    annotations = set()
    if is_oop or file_path.endswith(".py"):
        anns = re.findall(r"@([a-zA-Z0-9_]+)", file_content)
        for a in anns:
            annotations.add(a.lower())

    term_counts = {}
    for t in query_terms:
        count = 0
        for ct in content_tokens_list:
            if t == ct:
                count += 1
            elif len(t) >= 2 and (t in ct or (len(ct) >= 2 and ct in t)):
                count += 1
        if count > 0:
            term_counts[t] = count
            
    matched = list(term_counts.keys())

    if not query_terms:
        return 0.0, []

    # Multiplier strength scales inversely with query length.
    # Short queries (1-2 terms, likely vibe) need a loud structural signal.
    # Long queries (4+ terms, likely standard LLM) rely more on BM25 math.
    n_terms = len(query_terms)
    if n_terms <= 2:
        class_mult = 10.0
        ann_mult = 5.0
    elif n_terms <= 4:
        class_mult = 6.0
        ann_mult = 3.0
    else:
        class_mult = 3.0
        ann_mult = 2.0

    score = 0.0
    for t in matched:
        base_weight = idf_weights.get(t, 1.0)
        multiplier = 1.0
        
        # 3. Apply Multipliers — TS exports always get 8x regardless of query length
        if t in ts_exports:
            multiplier = 8.0
        elif t in declared_classes:
            multiplier = class_mult
        elif t in java_methods or t in py_defs:
            multiplier = 4.0
        elif t in annotations:
            multiplier = ann_mult
            
        # 4. BM25 Term Frequency
        count = term_counts[t]
        k1 = 1.5
        b = 0.75
        tf_bm25 = (count * (k1 + 1)) / (count + k1 * (1 - b + b * (dl / avgdl)))
            
        score += (tf_bm25 * base_weight * multiplier)

    max_score = sum(idf_weights.get(t, 1.0) for t in query_terms)
    if max_score > 0:
        base_normalized = min(1.0, sum(idf_weights.get(t, 1.0) for t in matched) / max_score)
        bonus = score - sum(idf_weights.get(t, 1.0) for t in matched)
        final_score = base_normalized + bonus
    else:
        final_score = 0.0

    return final_score, matched


def _apply_neighbor_bonus(
    scores: dict[str, float],
    repo_graph: RepoGraph,
    boost: float = 0.2,
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

    # --- Pre-computation: Global TF-IDF & BM25 ---
    total_files = len(repo_graph.nodes)
    document_frequency = {term: 0 for term in query_terms}
    
    total_tokens_count = 0
    
    for path, node in repo_graph.nodes.items():
        content = node.content
        dl = node.doc_length
        total_tokens_count += dl
        
        raw_tokens = re.findall(r"[a-z0-9]+", content.lower())
        content_tokens = set(raw_tokens)
        
        if path.endswith(".java"):
            camel_tokens = []
            for word in re.findall(r"[a-zA-Z]+", content):
                if any(c.isupper() for c in word):
                    sub = re.sub(r"([A-Z])", r" \1", word).lower()
                    camel_tokens.extend(re.findall(r"[a-z0-9]+", sub))
            content_tokens.update([t for t in camel_tokens if len(t) > 1])
            
        path_tokens = set(_path_tokens(path))
        combined_tokens = content_tokens.union(path_tokens)
        for term in query_terms:
            if any(_is_match(term, ct) for ct in combined_tokens):
                document_frequency[term] += 1

    avgdl = total_tokens_count / total_files if total_files > 0 else 1.0

    idf_weights = {}
    for term in query_terms:
        df = document_frequency[term]
        if df == 0:
            idf_weights[term] = 0.0
        else:
            idf_weights[term] = max(0.1, math.log(total_files / (1 + df))) if total_files > 0 else 1.0

    # --- Pass 1: keyword + content scores per file ---
    base_scores: dict[str, float] = {}
    keyword_scores: dict[str, float] = {}
    content_scores: dict[str, float] = {}
    matched_terms: dict[str, list[str]] = {}

    for path, node in repo_graph.nodes.items():
        kscore, kterms = _keyword_score(query_terms, path, idf_weights)
        dl = node.doc_length
        cscore, cterms = _content_score(query_terms, path, node.content, idf_weights, dl, avgdl)

        keyword_scores[path] = kscore
        content_scores[path] = cscore
        matched_terms[path] = list(set(kterms + cterms))
        
        # Base combination: heavily weight filename/path matches (70%) over content matches (30%)
        # This prevents transitive consumers of a file from out-ranking the file itself
        combined = (kscore * 0.7) + (cscore * 0.3)
        
        # Tiebreaker: Slightly penalize deep paths so src/x.py wins over build/npm/python/x.py
        depth_penalty = 0.0001 * path.count("/")
        combined -= depth_penalty
        
        base_scores[path] = combined

    # --- Pass 2: neighbor bonus ---
    boosted_scores = _apply_neighbor_bonus(base_scores, repo_graph)

    # --- Pass 3: centrality tiebreaker ---
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

    # Down-rank test files unless the user specifically searched for tests
    is_test_query = "test" in q.lower() or "spec" in q.lower()
    for r in results:
        if _is_test_file(r.path) and not is_test_query:
            r.total_score *= 0.5

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
