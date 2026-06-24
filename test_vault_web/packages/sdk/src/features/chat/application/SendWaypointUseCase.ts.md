# SendWaypointUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/application/SendWaypointUseCase.ts`
- **Extension:** `.ts`
- **Size:** 1135 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Destination`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/identifiers/PacketId.ts.md|packages/sdk/src/core/identifiers/PacketId.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { generatePacketId } from "../../../core/identifiers/PacketId.ts";
import {
  ChannelNumber,
  type Destination,
  Emitter,
} from "../../../core/types.ts";

export async function sendWaypoint(
  client: MeshClient,
  waypoint: Protobuf.Mesh.Waypoint,
  destination: Destination,
  channel: ChannelNumber = ChannelNumber.Primary,
): Promise<ResultType<number, Error>> {
  client.log.debug(
    Emitter[Emitter.SendWaypoint],
...
```