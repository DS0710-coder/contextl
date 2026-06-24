# sdkClient.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/connections/sdkClient.ts`
- **Extension:** `.ts`
- **Size:** 3471 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AnyTransport`

## Imports (Dependencies)
- [[apps/web/src/core/sdkStorage.ts.md|apps/web/src/core/sdkStorage.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/transport-http/mod.ts.md|packages/transport-http/mod.ts]]
- [[packages/transport-web-bluetooth/mod.ts.md|packages/transport-web-bluetooth/mod.ts]]
- [[packages/transport-web-serial/mod.ts.md|packages/transport-web-serial/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import { coordinator, getStorageDb } from "@core/sdkStorage.ts";
import type { ConnectionId } from "@core/stores/deviceStore/types";
import { createLogger, MeshDevice } from "@meshtastic/sdk";
import {
  SqlocalDraftRepository,
  SqlocalMessageRepository,
} from "@meshtastic/sdk-storage-sqlocal/chat";
import { SqlocalNodesRepository } from "@meshtastic/sdk-storage-sqlocal/nodes";
import { SqlocalTelemetryRepository } from "@meshtastic/sdk-storage-sqlocal/telemetry";
import type { TransportHTTP } from "@meshtastic/transport-http";
import type { TransportWebBluetooth } from "@meshtastic/transport-web-bluetooth";
import type { TransportWebSerial } from "@meshtastic/transport-web-serial";

const log = createLogger("sdkClient");

export type AnyTransport =
  | TransportHTTP
  | TransportWebBluetooth
  | TransportWebSerial;

...
```