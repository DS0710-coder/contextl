import sys, os, traceback
sys.path.insert(0, os.path.abspath("src"))
from mcp_server import _get_graph
from impact_analysis import analyze_impact

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

for repo_path in repos:
    print(f"\n--- Testing {os.path.basename(repo_path)} ---")
    try:
        scan, repo_graph = _get_graph(repo_path)
    except Exception as e:
        continue
        
    nodes = list(repo_graph.nodes.keys())
    for node in nodes:
        try:
            report = analyze_impact(node, repo_graph, max_depth=5)
        except Exception as e:
            print(f"BUG on {node} in {os.path.basename(repo_path)}: {e}")
            
print("All impact analyses finished.")
