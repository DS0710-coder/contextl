# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/index.ts`
- **Extension:** `.ts`
- **Size:** 195 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]
- [[packages/sdk/src/features/device/domain/Device.ts.md|packages/sdk/src/features/device/domain/Device.ts]]
- [[packages/sdk/src/features/device/domain/DeviceStatus.ts.md|packages/sdk/src/features/device/domain/DeviceStatus.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { DeviceClient } from "./DeviceClient.ts";
export type { Device } from "./domain/Device.ts";
export {
  DeviceStatusEnum,
  isConfigured,
  isConnected,
} from "./domain/DeviceStatus.ts";
```