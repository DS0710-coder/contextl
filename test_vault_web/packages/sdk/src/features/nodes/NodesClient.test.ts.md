# NodesClient.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/NodesClient.test.ts`
- **Extension:** `.ts`
- **Size:** 2073 bytes
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

describe("NodesClient", () => {
  it("populates the list signal from incoming NodeInfo packets", async () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });

    expect(client.nodes.list.value).toEqual([]);

    client.events.onNodeInfoPacket.dispatch(
      create(Protobuf.Mesh.NodeInfoSchema, { num: 1 }),
    );
    client.events.onNodeInfoPacket.dispatch(
      create(Protobuf.Mesh.NodeInfoSchema, { num: 2, isFavorite: true }),
    );
...
```