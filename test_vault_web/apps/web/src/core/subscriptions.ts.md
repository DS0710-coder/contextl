# subscriptions.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/subscriptions.ts`
- **Extension:** `.ts`
- **Size:** 4186 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useNewNodeNum.ts.md|apps/web/src/core/hooks/useNewNodeNum.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import { useNewNodeNum } from "@core/hooks/useNewNodeNum";
import { type Device } from "@core/stores";
import { type MeshDevice, Protobuf } from "@meshtastic/sdk";

/**
 * Wires up the legacy MeshDevice event stream into the web's Zustand stores.
 *
 * Note: the SDK now owns chat persistence (via SqlocalMessageRepository) and
 * the entire NodesClient surface — node info, user, position, lastHeard /
 * snr, favourite / ignored flags, and PKI-error tracking. This handler no
 * longer mirrors any of that into the legacy stores; what remains is
 * device-store-only state (waypoints, traceroutes, neighbour info, dialog
 * open triggers, unread counts).
 */
export const subscribeAll = (device: Device, connection: MeshDevice) => {
  connection.events.onDeviceMetadataPacket.subscribe((metadataPacket) => {
    device.addMetadata(metadataPacket.from, metadataPacket.data);
  });

  connection.events.onRoutingPacket.subscribe((routingPacket) => {
...
```