# MeshClientPort.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/core/client/MeshClientPort.ts`
- **Extension:** `.ts`
- **Size:** 1321 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Subscribable`
- `MeshClientEvents`
- `MeshClientPort`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts.md|apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
import type { Protobuf, Types } from "@meshtastic/core";

/**
 * Minimal subscribe-only view of an event source. `ste-simple-events`'
 * `SimpleEventDispatcher` (used by the legacy `MeshDevice`) satisfies this, as
 * does a preact signal facade — so the slice doesn't care where events come
 * from.
 */
export interface Subscribable<T> {
  subscribe(listener: (value: T) => void): unknown;
}

/** The subset of device events the config slice subscribes to. */
export interface MeshClientEvents {
  onConfigPacket: Subscribable<Protobuf.Config.Config>;
  onModuleConfigPacket: Subscribable<Protobuf.ModuleConfig.ModuleConfig>;
  onDeviceStatus: Subscribable<Types.DeviceStatusEnum>;
}

/**
...
```