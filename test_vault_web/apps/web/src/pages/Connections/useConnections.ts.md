# useConnections.ts

## Architecture Metrics
- **Path:** `apps/web/src/pages/Connections/useConnections.ts`
- **Extension:** `.ts`
- **Size:** 14052 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useConnections`

## Imports (Dependencies)
- [[apps/web/src/core/connections/heartbeat.ts.md|apps/web/src/core/connections/heartbeat.ts]]
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]
- [[apps/web/src/core/meshRegistry.ts.md|apps/web/src/core/meshRegistry.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/subscriptions.ts.md|apps/web/src/core/subscriptions.ts]]
- [[apps/web/src/core/utils/randId.ts.md|apps/web/src/core/utils/randId.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```ts
import {
  startConfigHeartbeat,
  startMaintenanceHeartbeat,
  stopHeartbeat,
} from "@app/core/connections/heartbeat.ts";
import { buildMeshDevice } from "@app/core/connections/sdkClient.ts";
import {
  closeTransport,
  openTransport,
  probeConnection,
} from "@app/core/connections/transports.ts";
import { createLogger, DeviceStatusEnum } from "@meshtastic/sdk";

const log = createLogger("useConnections");
import type {
  Connection,
  ConnectionId,
  ConnectionStatus,
  NewConnection,
} from "@app/core/stores/deviceStore/types";
...
```