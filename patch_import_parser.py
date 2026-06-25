import re

with open("src/import_parser.py", "r") as f:
    text = f.read()

GO_AND_CPP_HANDLERS = """
def _skeleton_go(root: "Node") -> dict:
    classes = []
    functions = []
    exports = []
    docstrings = {}

    def visit_fn(node: "Node") -> dict:
        name = ""
        params = ""
        ret_type = ""
        is_method = (node.type == "method_declaration")
        receiver = ""

        for child in node.children:
            if child.type == "identifier" or child.type == "field_identifier":
                if not name:
                    name = _node_text(child)
            elif child.type == "parameter_list":
                if is_method and not receiver:
                    receiver = _node_text(child)
                else:
                    params = _node_text(child)
            elif child.type == "type_identifier":
                ret_type = _node_text(child)

        return {"name": name, "params": params, "return_type": ret_type, "visibility": "pub" if name and name[0].isupper() else "private", "is_async": False, "decorators": [], "receiver": receiver}

    def visit(node: "Node"):
        if node.type in ("function_declaration", "method_declaration"):
            functions.append(visit_fn(node))
        elif node.type == "type_spec":
            name = ""
            for child in node.children:
                if child.type == "type_identifier":
                    name = _node_text(child)
                elif child.type == "struct_type" or child.type == "interface_type":
                    if name:
                        classes.append({"name": name, "fields": [], "methods": [], "extends": "", "implements": [], "properties": []})
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}

def _skeleton_cpp(root: "Node") -> dict:
    classes = []
    functions = []
    exports = []
    docstrings = {}

    def visit_fn(node: "Node") -> dict:
        name = ""
        params = ""
        for child in node.children:
            if child.type == "function_declarator":
                for sub in child.children:
                    if sub.type == "identifier" or sub.type == "field_identifier":
                        name = _node_text(sub)
                    elif sub.type == "parameter_list":
                        params = _node_text(sub)
        return {"name": name, "params": params, "return_type": "", "visibility": "pub", "is_async": False, "decorators": []}

    def visit(node: "Node"):
        if node.type == "function_definition":
            functions.append(visit_fn(node))
        elif node.type in ("class_specifier", "struct_specifier"):
            name = ""
            for child in node.children:
                if child.type == "type_identifier":
                    name = _node_text(child)
            if name:
                classes.append({"name": name, "fields": [], "methods": [], "extends": "", "implements": [], "properties": []})
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}
"""

text = text.replace("_SKELETON_HANDLERS = {", GO_AND_CPP_HANDLERS + "\n_SKELETON_HANDLERS = {")

# Register handlers
text = text.replace(
    '".rs": _skeleton_rust,',
    '".rs": _skeleton_rust,\n    ".go": _skeleton_go,\n    ".cpp": _skeleton_cpp,\n    ".h": _skeleton_cpp,\n    ".hpp": _skeleton_cpp,\n    ".cc": _skeleton_cpp,\n    ".c": _skeleton_cpp,'
)

with open("src/import_parser.py", "w") as f:
    f.write(text)

print("Patched import_parser.py")
