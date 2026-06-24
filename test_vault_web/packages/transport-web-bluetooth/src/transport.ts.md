# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-web-bluetooth/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 11001 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `BluetoothConnectError`
- `isTransientGattFailure`
- `toArrayBuffer`
- `TransportWebBluetooth`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-web-bluetooth/mod.ts.md|packages/transport-web-bluetooth/mod.ts]]
- [[packages/transport-web-bluetooth/src/transport.test.ts.md|packages/transport-web-bluetooth/src/transport.test.ts]]

## Source Code Snippet
```ts
import {
  DeviceStatusEnum,
  type DeviceOutput,
  type Transport,
} from "@meshtastic/sdk";

/**
 * Typed error thrown when establishing the GATT connection fails. `kind`
 * lets callers distinguish recoverable transients (BT stack hiccup, device
 * just woke from sleep) from fatal states (out of range, no service).
 *
 * `userMessage` is a human-readable, actionable string suitable for
 * surfacing in UI without further interpretation.
 */
export class BluetoothConnectError extends Error {
  public readonly kind: "transient" | "unavailable" | "missing-service";
  public readonly userMessage: string;

  constructor(
    kind: BluetoothConnectError["kind"],
...
```