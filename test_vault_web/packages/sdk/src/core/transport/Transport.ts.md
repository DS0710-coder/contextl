# Transport.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/transport/Transport.ts`
- **Extension:** `.ts`
- **Size:** 782 bytes
- **Centrality Score:** 0.0361
- **In-Degree (Imported By):** 13
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Packet`
- `DebugLog`
- `StatusEvent`
- `DeviceOutput`
- `Transport`
- `HttpRetryConfig`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/core/packet-codec/fromDevice.ts.md|packages/sdk/src/core/packet-codec/fromDevice.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/transport/index.ts.md|packages/sdk/src/core/transport/index.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/config/ConfigEditor.test.ts.md|packages/sdk/src/features/config/ConfigEditor.test.ts]]
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]
- [[packages/sdk/src/features/device/domain/DeviceStatus.ts.md|packages/sdk/src/features/device/domain/DeviceStatus.ts]]
- [[packages/sdk/src/features/device/state/deviceStore.ts.md|packages/sdk/src/features/device/state/deviceStore.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]

## Source Code Snippet
```ts
export enum DeviceStatusEnum {
  DeviceRestarting = 1,
  DeviceDisconnected = 2,
  DeviceConnecting = 3,
  DeviceReconnecting = 4,
  DeviceConnected = 5,
  DeviceConfiguring = 6,
  DeviceConfigured = 7,
  DeviceError = 8,
}

interface Packet {
  type: "packet";
  data: Uint8Array;
}

interface DebugLog {
  type: "debug";
  data: string;
}
...
```