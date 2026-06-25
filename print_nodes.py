import sys
from pathlib import Path
sys.path.insert(0, str(Path("/home/dev7shah/Desktop/contextl/src").resolve()))
from import_parser import _get_parser

def print_tree(node, depth=0):
    print("  " * depth + node.type)
    for c in node.children:
        print_tree(c, depth+1)

ext = sys.argv[1]
parser, _ = _get_parser(ext)
source = Path(sys.argv[2]).read_bytes()
tree = parser.parse(source)
print_tree(tree.root_node)
