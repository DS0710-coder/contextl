# transports.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/connections/transports.ts`
- **Extension:** `.ts`
- **Size:** 9088 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `OpenTransportOptions`
- `OpenTransportResult`
- `closeTransport`

## Imports (Dependencies)
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/transport-http/mod.ts.md|packages/transport-http/mod.ts]]
- [[packages/transport-web-bluetooth/mod.ts.md|packages/transport-web-bluetooth/mod.ts]]
- [[packages/transport-web-serial/mod.ts.md|packages/transport-web-serial/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import type { Connection } from "@core/stores/deviceStore/types";
import { testHttpReachable } from "@pages/Connections/utils";
import { createLogger } from "@meshtastic/sdk";
import { TransportHTTP } from "@meshtastic/transport-http";
import {
  BluetoothConnectError,
  TransportWebBluetooth,
} from "@meshtastic/transport-web-bluetooth";
import {
  SerialConnectError,
  TransportWebSerial,
} from "@meshtastic/transport-web-serial";
import { Result } from "better-result";
import type { AnyTransport } from "./sdkClient.ts";

const log = createLogger("transports");

/**
 * Per-transport-type factories. Each resolves a Transport from a saved
 * Connection record + an optional cached BluetoothDevice/SerialPort the
...
```