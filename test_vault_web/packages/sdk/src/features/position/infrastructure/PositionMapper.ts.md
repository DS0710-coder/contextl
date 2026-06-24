# PositionMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/infrastructure/PositionMapper.ts`
- **Extension:** `.ts`
- **Size:** 482 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/position/domain/Position.ts.md|packages/sdk/src/features/position/domain/Position.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]
- [[packages/sdk/src/features/position/index.ts.md|packages/sdk/src/features/position/index.ts]]

## Source Code Snippet
```ts
import type { PacketMetadata } from "../../../core/types.ts";
import type * as Protobuf from "@meshtastic/protobufs";
import type { Position } from "../domain/Position.ts";

export const PositionMapper = {
  fromPacket(packet: PacketMetadata<Protobuf.Mesh.Position>): Position {
    return {
      nodeNum: packet.from,
      latitudeI: packet.data.latitudeI,
      longitudeI: packet.data.longitudeI,
      altitude: packet.data.altitude,
      time: packet.rxTime,
    };
  },
};
```