# messaging.direct.spec.ts

## Architecture Metrics
- **Path:** `e2e/tests/messaging.direct.spec.ts`
- **Extension:** `.ts`
- **Size:** 2196 bytes
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
import { peerNodeNum, startPeerRecv } from "../fixtures/peer.ts";
import { expect, test } from "../fixtures/test.ts";

/**
 * Direct (node-addressed) messaging across the real two-node mesh.
 *
 * NOTE: marked fixme — this is a SIMULATOR limitation, not a web-app issue, and
 * it bottoms out in the firmware's SimRadio:
 *   - DMs go out PKI-encrypted. PKI key generation is gated on a set LoRa region
 *     (NodeDB.cpp:3051 — keygen is skipped while region == UNSET) and the sim
 *     nodes boot region-UNSET. Setting `lora.region` via admin DOES fix key gen
 *     + exchange (verified: both nodes learn each other's public key).
 *   - But a PKI-encrypted DM still can't traverse the SimRadio: the PKC overhead
 *     pushes the packet past the SimRadio payload limit ("Payload size larger
 *     than compressed message allows! Send empty payload"), so it is truncated
 *     and the receiver can't decode it ("No suitable channel found for decoding,
 *     hash 0x0") -> NO_CHANNEL. The firmware deliberately skips PKC under the
 *     --sim flag (Router.cpp:730) for exactly this reason, but --sim also
 *     disables config-file loading (Webserver/EnableUDP/MAC) that the web app's
 *     HTTP API + UDP mesh require, so the two are mutually exclusive.
...
```