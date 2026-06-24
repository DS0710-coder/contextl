# PositionClient.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/PositionClient.test.ts`
- **Extension:** `.ts`
- **Size:** 1027 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../core/types.ts";

describe("PositionClient", () => {
  it("tracks per-node positions from packets", () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });

    client.events.onPositionPacket.dispatch({
      id: 1,
      from: 5,
      to: 5,
      channel: ChannelNumber.Primary,
      type: "direct",
      rxTime: new Date(1000),
      data: create(Protobuf.Mesh.PositionSchema, {
...
```