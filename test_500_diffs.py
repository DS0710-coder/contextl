import sys, os, subprocess, traceback
sys.path.insert(0, os.path.abspath("src"))

from mcp_server import _get_graph
from git_review import build_review_context

repo_path = "/home/dev7shah/Desktop/testfiles/go-ethereum-master./go-ethereum-master"
print(f"Building base graph for {repo_path}...")
scan, repo_graph = _get_graph(repo_path)
print("Graph built. Nodes:", len(repo_graph.nodes))

print("Fetching last 500 commits...")
commits_output = subprocess.check_output(
    ["git", "log", "-n", "500", "--pretty=format:%h"],
    cwd=repo_path, text=True
)
commits = commits_output.strip().split("\n")

success = 0
errors = 0
bug_reports = []

for i, commit in enumerate(commits):
    try:
        files_output = subprocess.check_output(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit],
            cwd=repo_path, text=True
        )
        changed_files = [f for f in files_output.strip().split("\n") if f]
        
        # Only keep files that exist in the graph (since we didn't checkout, old deleted files might not be there)
        valid_files = [f for f in changed_files if f in repo_graph.nodes]
        
        if not valid_files:
            continue
            
        context = build_review_context(repo_graph, valid_files)
        success += 1
    except Exception as e:
        errors += 1
        bug = f"Commit {commit} with files {valid_files} failed: {traceback.format_exc()}"
        bug_reports.append(bug)

print(f"\nTested {success+errors} commits. Success: {success}, Errors: {errors}")
for bug in bug_reports[:5]:
    print(bug)
    print("-" * 50)
