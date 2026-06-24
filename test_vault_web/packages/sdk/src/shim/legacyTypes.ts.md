# legacyTypes.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/shim/legacyTypes.ts`
- **Extension:** `.ts`
- **Size:** 607 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
Backwards-compatible re-export of the cross-cutting types under the
`Types` namespace. mod.ts already exports `Types` directly from
`core/types.ts`; this file is no longer wired anywhere but is kept as a
stable import path for any third-party that grabbed it via the published
dist.

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
/**
 * Backwards-compatible re-export of the cross-cutting types under the
 * `Types` namespace. mod.ts already exports `Types` directly from
 * `core/types.ts`; this file is no longer wired anywhere but is kept as a
 * stable import path for any third-party that grabbed it via the published
 * dist.
 */
export type {
  Destination,
  DeviceOutput,
  HttpRetryConfig,
  LogEvent,
  LogEventPacket,
  PacketDestination,
  PacketError,
  PacketMetadata,
  QueueItem,
  Transport,
} from "../core/types.ts";
export {
...
```