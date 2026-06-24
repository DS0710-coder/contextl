# peer.py

## Architecture Metrics
- **Path:** `e2e/peer/peer.py`
- **Extension:** `.py`
- **Size:** 4900 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `log`
- `emit`
- `connect`
- `cmd_node_num`
- `cmd_send`
- `cmd_recv`
- `on_text`
- `main`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```py
#!/usr/bin/env python3
"""Standalone Meshtastic test peer for the web E2E suite.

Connects to a `meshtasticd` node over the TCP phone API and either sends a text
message, blocks until a specific text is received, or prints the node's own
number. It mirrors the `wait_for(predicate, timeout)` + `send_text` conventions
from `firmware/mcp-server/tests/mesh/_receive.py`, but uses `TCPInterface` so it
can talk to a daemon (that `ReceiveCollector` is serial-only).

Machine-readable stdout markers (everything else goes to stderr):
  - `node-num`  -> `NODE_NUM=<n>`
  - `recv`      -> `READY` once subscribed, then `RECEIVED=<from>` on match

Exit codes: 0 success, 1 timeout / not received, 2 usage / connection error.

Usage:
  peer.py --host localhost --port 4404 send "hello" [--to <nodenum>] [--want-ack]
  peer.py --host localhost --port 4403 recv "hello" [--from-node <n>] [--timeout 60]
  peer.py --host localhost --port 4404 node-num
"""
...
```