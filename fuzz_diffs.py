import sys, os, random, traceback
sys.path.insert(0, os.path.abspath("src"))
from mcp_server import _get_graph
from git_review import build_review_context

testfiles_dir = "/home/dev7shah/Desktop/testfiles"
repos = []
for entry in os.listdir(testfiles_dir):
    full_path = os.path.join(testfiles_dir, entry)
    if os.path.isdir(full_path):
        nested = os.path.join(full_path, entry.replace(".", ""))
        if os.path.isdir(nested):
            repos.append(nested)
        else:
            repos.append(full_path)

total_success = 0
total_errors = 0
bug_reports = []

for repo_path in repos:
    try:
        scan, repo_graph = _get_graph(repo_path)
    except Exception as e:
        continue
        
    nodes = list(repo_graph.nodes.keys())
    if not nodes:
        continue
        
    for _ in range(100):
        num_files = random.randint(1, 20)
        modified_files = random.sample(nodes, min(num_files, len(nodes)))
        try:
            build_review_context(repo_path, set(modified_files), set(), repo_graph)
            total_success += 1
        except Exception as e:
            total_errors += 1
            bug_reports.append(f"Repo: {os.path.basename(repo_path)} | Files: {modified_files[:3]}... | Error: {traceback.format_exc()}")

print(f"\n=== FUZZING COMPLETE ===")
print(f"Success: {total_success}, Errors: {total_errors}")
for bug in bug_reports[:10]:
    print(bug)
    print("-" * 50)
