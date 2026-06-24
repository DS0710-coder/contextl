# legacyUtils.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/shim/legacyUtils.ts`
- **Extension:** `.ts`
- **Size:** 469 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
Re-exports for the public `Utils` namespace (mod.ts: `export * as Utils`).
Transport packages import `toDeviceStream` / `fromDeviceStream` here.

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/packet-codec/fromDevice.ts.md|packages/sdk/src/core/packet-codec/fromDevice.ts]]
- [[packages/sdk/src/core/packet-codec/toDevice.ts.md|packages/sdk/src/core/packet-codec/toDevice.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/core/xmodem/Xmodem.ts.md|packages/sdk/src/core/xmodem/Xmodem.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
/**
 * Re-exports for the public `Utils` namespace (mod.ts: `export * as Utils`).
 * Transport packages import `toDeviceStream` / `fromDeviceStream` here.
 */
export { EventBus as EventSystem } from "../core/event-bus/EventBus.ts";
export { Queue } from "../core/queue/Queue.ts";
export { Xmodem } from "../core/xmodem/Xmodem.ts";
export { fromDeviceStream } from "../core/packet-codec/fromDevice.ts";
export { toDeviceStream } from "../core/packet-codec/toDevice.ts";
```