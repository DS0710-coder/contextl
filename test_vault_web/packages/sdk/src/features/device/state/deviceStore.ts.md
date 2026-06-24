# deviceStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/state/deviceStore.ts`
- **Extension:** `.ts`
- **Size:** 1037 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createDeviceStore`
- `DeviceStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import { createStore } from "../../../core/signals/createStore.ts";
import { DeviceStatusEnum } from "../../../core/transport/Transport.ts";

/**
 * Writable signals for the device slice. Only the slice application layer
 * mutates these; callers consume the `.read` readonly facades exposed by
 * DeviceClient.
 */
export function createDeviceStore() {
  const status = createStore<DeviceStatusEnum>(
    DeviceStatusEnum.DeviceDisconnected,
  );
  const isConfigured = createStore(false);
  const pendingSettingsChanges = createStore(false);
  const myNodeNum = createStore<number | undefined>(undefined);
  const metadata = createStore<Protobuf.Mesh.DeviceMetadata | undefined>(
    undefined,
  );
  const myNodeInfo = createStore<Protobuf.Mesh.MyNodeInfo | undefined>(
...
```