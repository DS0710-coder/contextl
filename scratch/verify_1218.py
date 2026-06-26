import sys
from pathlib import Path
sys.path.insert(0, str(Path("src").resolve()))
from mcp_server import _run_query, _run_export_obsidian, _run_review_changes

repo = "/home/dev7shah/Desktop/testfiles/go-ethereum-master./go-ethereum-master"

# 1. Test Query Caching (should only build graph once)
print("Query 1...")
_run_query(repo, "test", 5)
print("Query 2 (should be instant)...")
_run_query(repo, "test 2", 5)

# 2. Test Obsidian Export
print("\nExporting Obsidian...")
try:
    res = _run_export_obsidian(repo, "scratch/obsidian_vault")
    print(f"Export success: {res.get('success', False)}")
except Exception as e:
    print(f"Export error: {e}")

# 3. Test git review without git
# We will temporarily mock subprocess.run to raise FileNotFoundError
import subprocess
_original_run = subprocess.run
def mock_run(*args, **kwargs):
    if args[0][0] == "git":
        raise FileNotFoundError("No git")
    return _original_run(*args, **kwargs)

subprocess.run = mock_run

print("\nRunning git review without git...")
res = _run_review_changes(repo, True, True)
print(f"Git review result: {res}")
