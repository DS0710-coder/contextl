# fromMeshDevice.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/adapters/fromMeshDevice.ts`
- **Extension:** `.ts`
- **Size:** 1602 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `meshDeviceToPort`
- `getConfigEditor`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/index.ts.md|apps/web/src/sdk-preview/index.ts]]
- [[apps/web/src/sdk-preview/react/useConfigEditor.ts.md|apps/web/src/sdk-preview/react/useConfigEditor.ts]]

## Source Code Snippet
```ts
import type { MeshDevice } from "@meshtastic/core";
import type { MeshClientPort } from "../core/index.ts";
import { ConfigEditor } from "../features/config/index.ts";

/**
 * Adapts the legacy `@meshtastic/core` `MeshDevice` to the slice's
 * `MeshClientPort`.
 *
 * In the real SDK (PR #1050) the client owns explicit begin/commit admin
 * messages. The legacy `MeshDevice.setConfig` already opens the edit
 * transaction itself (guarded by its `pendingSettingsChanges` flag) and
 * `commitEditSettings()` closes it — so `beginEditSettings` here is a no-op and
 * the transaction is driven by the existing device methods.
 */
export function meshDeviceToPort(device: MeshDevice): MeshClientPort {
  return {
    events: {
      onConfigPacket: device.events.onConfigPacket,
      onModuleConfigPacket: device.events.onModuleConfigPacket,
      onDeviceStatus: device.events.onDeviceStatus,
...
```