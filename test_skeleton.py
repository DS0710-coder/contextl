import sys
from pathlib import Path
sys.path.insert(0, str(Path("src").resolve()))
from import_parser import extract_skeleton
import json

file_path = sys.argv[1]
print(json.dumps(extract_skeleton(file_path), indent=2))
