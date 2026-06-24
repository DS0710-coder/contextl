import sys
import os

sys.path.insert(0, '/home/dev7shah/.nvm/versions/node/v24.15.0/lib/node_modules/contextl/python')
from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query as search_codebase
from impact_analysis import analyze_impact
from dead_code import find_dead_files

path = "/home/dev7shah/Desktop/testfiles/libreplan-main./libreplan-main"

print("--- 1. SCAN ---")
scan = scan_repo(path)
print(f"Scanned files: {len(scan.files)}")

print("\n--- 2. PARSE & GRAPH ---")
parse = parse_imports(scan)
rg = build_graph(scan, parse)
print(f"Relationships: {len(parse.relationships)}")
print(f"Unresolved imports (external/std lib): {len(parse.unresolved)}")

print("\n--- 3. SEARCH ---")
results = search_codebase("login auth", rg)
print(f"Top 3 results for 'login auth':")
for r in results[:3]:
    print(f"  - {r.path} (score: {r.total_score:.3f})")

print("\n--- 4. IMPACT ANALYSIS ---")
target = "libreplan-webapp/src/main/java/org/libreplan/web/users/UserCRUDController.java"
impact = analyze_impact(target, rg)
print(f"Impact of {os.path.basename(target)}:")
print(f"  - Directly affected: {len(impact.directly_affected)}")
print(f"  - Transitively affected: {len(impact.transitively_affected)}")
print(f"  - Total: {impact.total_affected}")
print("  Sample of directly affected files:")
for f in impact.directly_affected[:5]:
    print(f"    - {f.path}")

print("\n--- 5. DEAD CODE ---")
dead = find_dead_files(rg)
print(f"Total dead files: {len(dead)}")
print(f"Sample of dead files:")
for d in list(dead)[:5]:
    print(f"  - {d}")

