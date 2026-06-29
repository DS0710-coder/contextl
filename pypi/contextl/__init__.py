import importlib.metadata

try:
    __version__ = importlib.metadata.version("contextl-mcp")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"
