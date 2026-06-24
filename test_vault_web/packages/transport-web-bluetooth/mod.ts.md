# mod.ts

## Architecture Metrics
- **Path:** `packages/transport-web-bluetooth/mod.ts`
- **Extension:** `.ts`
- **Size:** 88 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/transport-web-bluetooth/src/transport.ts.md|packages/transport-web-bluetooth/src/transport.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]

## Source Code Snippet
```ts
export {
  BluetoothConnectError,
  TransportWebBluetooth,
} from "./src/transport.ts";
```