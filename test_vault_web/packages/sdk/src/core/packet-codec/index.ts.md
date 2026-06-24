# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/packet-codec/index.ts`
- **Extension:** `.ts`
- **Size:** 203 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/core/packet-codec/fromDevice.ts.md|packages/sdk/src/core/packet-codec/fromDevice.ts]]
- [[packages/sdk/src/core/packet-codec/toDevice.ts.md|packages/sdk/src/core/packet-codec/toDevice.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
export { fromDeviceStream } from "./fromDevice.ts";
export { toDeviceStream } from "./toDevice.ts";
export { decodePacket } from "./decodePacket.ts";
export type { PacketSink } from "./decodePacket.ts";
```