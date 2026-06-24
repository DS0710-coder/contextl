# types.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/deviceStore/types.ts`
- **Extension:** `.ts`
- **Size:** 2113 bytes
- **Centrality Score:** 0.0063
- **In-Degree (Imported By):** 12
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ValidConfigType`
- `ValidModuleConfigType`
- `Dialogs`
- `DialogVariant`
- `Page`
- `ConnectionId`
- `ConnectionType`
- `ConnectionStatus`
- `Connection`
- `NewConnection`
- `WaypointWithMetadata`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx.md|apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx]]
- [[apps/web/src/core/connections/heartbeat.ts.md|apps/web/src/core/connections/heartbeat.ts]]
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/selectors.ts.md|apps/web/src/core/stores/deviceStore/selectors.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/sdk";

type ValidConfigType = Exclude<
  keyof Protobuf.LocalOnly.LocalConfig,
  "version" | "$typeName"
>;
type ValidModuleConfigType = Exclude<
  keyof Protobuf.LocalOnly.LocalModuleConfig,
  "version" | "$typeName"
>;

interface Dialogs {
  import: boolean;
  QR: boolean;
  shutdown: boolean;
  reboot: boolean;
  deviceName: boolean;
  nodeRemoval: boolean;
  pkiBackup: boolean;
  nodeDetails: boolean;
...
```