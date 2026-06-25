"""
contextl — entry point

Called when a user runs:
    contextl                   (console_scripts shim installed by pip)
    python -m contextl         (module execution)

Resolves the bundled mcp_server.py, sets up the environment, then uses
os.execve to *replace* the current process with Python running mcp_server.py.
This means no subprocess wrapper, no extra PID, and clean signal forwarding —
the IDE talks directly to mcp_server.py over stdio.
"""

import os
import sys
from pathlib import Path


def main() -> None:
    # The bundled engine files live in python/ next to this package.
    # Installed layout (wheel):
    #   site-packages/
    #     contextl/           ← this file lives here
    #     python/             ← engine files live here
    python_dir = Path(__file__).parent.parent / "python"
    mcp_server = python_dir / "mcp_server.py"

    if not mcp_server.exists():
        print(
            f"Error: cannot find mcp_server.py at {mcp_server}\n"
            "The package may be corrupted — try reinstalling:\n"
            "    pip install --force-reinstall contextl-mcp",
            file=sys.stderr,
        )
        sys.exit(1)

    env = os.environ.copy()
    env["PYTHONPATH"] = str(python_dir)
    env["PYTHONUNBUFFERED"] = "1"

    # Replace this process entirely — clean stdio passthrough, no extra PID.
    os.execve(sys.executable, [sys.executable, str(mcp_server)] + sys.argv[1:], env)


if __name__ == "__main__":
    main()
