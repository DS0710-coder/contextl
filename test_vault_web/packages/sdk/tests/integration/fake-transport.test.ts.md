# fake-transport.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/tests/integration/fake-transport.test.ts`
- **Extension:** `.ts`
- **Size:** 2574 bytes
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
import { MeshClient } from "../../src/core/client/MeshClient.ts";
import { createFakeTransport } from "../../src/core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../src/core/types.ts";

describe("MeshClient with fake transport", () => {
  it("wires MyNodeInfo → device.myNodeNum signal", async () => {
    const { transport, respond } = createFakeTransport();
    const client = new MeshClient({ transport });
    respond.withMyNodeInfo({ myNodeNum: 42 });
    await new Promise((r) => setTimeout(r, 10));
    expect(client.device.myNodeNum.value).toBe(42);
  });

  it("wires NodeInfo → nodes.list signal", async () => {
    const { transport, respond } = createFakeTransport();
    const client = new MeshClient({ transport });
    respond.withNodeInfo({ num: 1234 });
...
```