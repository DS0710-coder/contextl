# ChannelsClient.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/ChannelsClient.test.ts`
- **Extension:** `.ts`
- **Size:** 1112 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";

describe("ChannelsClient", () => {
  it("collects channels by index from onChannelPacket", () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });

    client.events.onChannelPacket.dispatch(
      create(Protobuf.Channel.ChannelSchema, {
        index: 0,
        role: Protobuf.Channel.Channel_Role.PRIMARY,
      }),
    );
    client.events.onChannelPacket.dispatch(
      create(Protobuf.Channel.ChannelSchema, {
        index: 1,
...
```