# useMeshDevice.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useMeshDevice.ts`
- **Extension:** `.ts`
- **Size:** 1254 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseMeshDeviceResult`
- `useMeshDevice`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { DeviceStatusEnum } from "@meshtastic/sdk";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseMeshDeviceResult {
  status: DeviceStatusEnum;
  isConfigured: boolean;
  myNodeNum: number | undefined;
  metadata: Protobuf.Mesh.DeviceMetadata | undefined;
  reboot(seconds?: number): Promise<number>;
  shutdown(seconds?: number): Promise<number>;
}

/**
 * Exposes the device slice of the current MeshClient: status, metadata, and
 * reboot/shutdown commands. Named `useMeshDevice` (not `useDevice`) so it does
 * not collide with consumer hooks of the same name (e.g. the legacy one in
 * `packages/web`).
 */
...
```