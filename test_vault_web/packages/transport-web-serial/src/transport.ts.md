# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-web-serial/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 13136 bytes
- **Centrality Score:** 0.0018
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `SerialConnectError`
- `isPortBusyError`
- `TransportWebSerial`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-web-serial/mod.ts.md|packages/transport-web-serial/mod.ts]]
- [[packages/transport-web-serial/src/transport.test.ts.md|packages/transport-web-serial/src/transport.test.ts]]

## Source Code Snippet
```ts
import {
  createLogger,
  DeviceStatusEnum,
  type DeviceOutput,
  fromDeviceStream,
  toDeviceStream,
  type Transport,
} from "@meshtastic/sdk";
import { Result, type ResultType } from "better-result";

const log = createLogger("TransportWebSerial");

/**
 * Typed error produced when preparing a `SerialPort` for use fails. `kind`
 * lets callers distinguish recoverable cases (port held briefly during
 * USB re-enumeration) from fatal ones (another tab or process owns the
 * port). `userMessage` is a human-readable, actionable string ready for
 * UI without further interpretation.
 */
export class SerialConnectError extends Error {
...
```