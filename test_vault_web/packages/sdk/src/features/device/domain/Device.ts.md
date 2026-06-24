# Device.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/domain/Device.ts`
- **Extension:** `.ts`
- **Size:** 399 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Device`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/device/index.ts.md|packages/sdk/src/features/device/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

/**
 * Aggregate representing a single connected device — its identity, status,
 * and hardware metadata.
 */
export interface Device {
  readonly myNodeNum: number;
  readonly hwModel?: Protobuf.Mesh.HardwareModel;
  readonly rebootCount?: number;
  readonly firmwareVersion?: string;
  readonly metadata?: Protobuf.Mesh.DeviceMetadata;
}
```