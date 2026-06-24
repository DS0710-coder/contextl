# PositionUseCases.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/application/PositionUseCases.ts`
- **Extension:** `.ts`
- **Size:** 2162 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { sendAdminMessage } from "../../device/infrastructure/AdminMessageSender.ts";

export async function setFixedPosition(
  client: MeshClient,
  latitude: number,
  longitude: number,
): Promise<ResultType<number, Error>> {
  try {
    const position = create(Protobuf.Mesh.PositionSchema, {
      latitudeI: Math.floor(latitude / 1e-7),
      longitudeI: Math.floor(longitude / 1e-7),
    });
    const id = await sendAdminMessage(
      client,
      { case: "setFixedPosition", value: position },
...
```