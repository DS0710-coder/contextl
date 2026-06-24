# peer.ts

## Architecture Metrics
- **Path:** `e2e/fixtures/peer.ts`
- **Extension:** `.ts`
- **Size:** 4247 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `spawnPeer`
- `onStdoutLines`
- `peerSend`
- `peerNodeNum`
- `RecvHandle`
- `startPeerRecv`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[e2e/tests/messaging.broadcast.spec.ts.md|e2e/tests/messaging.broadcast.spec.ts]]
- [[e2e/tests/messaging.direct.spec.ts.md|e2e/tests/messaging.direct.spec.ts]]

## Source Code Snippet
```ts
import { type ChildProcess, spawn } from "node:child_process";
import path from "node:path";

/**
 * Thin TypeScript wrapper around e2e/peer/peer.py — the off-browser "mesh peer"
 * that talks to the non-browser node over the TCP phone API. It sends text,
 * blocks until a specific text is received, or reports the node's number.
 */
const PYTHON = process.env.E2E_PEER_PYTHON ?? path.resolve("e2e/peer/.venv/bin/python");
const SCRIPT = path.resolve("e2e/peer/peer.py");
const HOST = process.env.E2E_PEER_HOST ?? "127.0.0.1";
const PORT = process.env.E2E_PEER_PORT ?? "14404";

function spawnPeer(args: string[]): ChildProcess {
  return spawn(PYTHON, [SCRIPT, "--host", HOST, "--port", PORT, ...args]);
}

/** Invoke `onLine` for each complete stdout line. */
function onStdoutLines(child: ChildProcess, onLine: (line: string) => void): void {
  let buf = "";
...
```