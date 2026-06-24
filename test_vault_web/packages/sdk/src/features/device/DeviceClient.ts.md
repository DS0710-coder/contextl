# DeviceClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/DeviceClient.ts`
- **Extension:** `.ts`
- **Size:** 2744 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/features/device/application/GetMetadataUseCase.ts.md|packages/sdk/src/features/device/application/GetMetadataUseCase.ts]]
- [[packages/sdk/src/features/device/application/RebootService.ts.md|packages/sdk/src/features/device/application/RebootService.ts]]
- [[packages/sdk/src/features/device/state/deviceStore.ts.md|packages/sdk/src/features/device/state/deviceStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/device/index.ts.md|packages/sdk/src/features/device/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import { DeviceStatusEnum } from "../../core/transport/Transport.ts";
import { reboot, rebootOta, shutdown } from "./application/RebootService.ts";
import { getMetadata } from "./application/GetMetadataUseCase.ts";
import { createDeviceStore, type DeviceStore } from "./state/deviceStore.ts";

/**
 * Device slice facade. Owns status/metadata signals and exposes the
 * reboot/shutdown/metadata commands.
 */
export class DeviceClient {
  private readonly store: DeviceStore;
  private readonly client: MeshClient;

  public readonly status: ReadonlySignal<DeviceStatusEnum>;
  public readonly isConfigured: ReadonlySignal<boolean>;
  public readonly pendingSettingsChanges: ReadonlySignal<boolean>;
  public readonly myNodeNum: ReadonlySignal<number | undefined>;
...
```