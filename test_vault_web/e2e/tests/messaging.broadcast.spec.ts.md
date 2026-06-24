# messaging.broadcast.spec.ts

## Architecture Metrics
- **Path:** `e2e/tests/messaging.broadcast.spec.ts`
- **Extension:** `.ts`
- **Size:** 1346 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[e2e/fixtures/peer.ts.md|e2e/fixtures/peer.ts]]
- [[e2e/fixtures/test.ts.md|e2e/fixtures/test.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { peerSend, startPeerRecv } from "../fixtures/peer.ts";
import { expect, test } from "../fixtures/test.ts";

/**
 * Broadcast text messaging across a real two-node mesh:
 *  - mesh -> web: the peer node broadcasts; the browser must render it.
 *  - web -> mesh: the browser sends; the peer node must receive it.
 * Both directions traverse real firmware over the UDP-multicast mesh.
 */
test.describe("broadcast messaging over a real two-node mesh", () => {
  test.beforeEach(async ({ connectionPage, messagesPage, device }) => {
    await connectionPage.connectHttp({ host: device.host, tls: device.tls });
    await messagesPage.waitReady();
  });

  test("renders a broadcast received from a mesh peer (mesh -> web)", async ({ messagesPage }) => {
    const nonce = `pong-${Date.now()}`;
    await peerSend(nonce);
    await messagesPage.expectMessage(nonce);
  });
...
```