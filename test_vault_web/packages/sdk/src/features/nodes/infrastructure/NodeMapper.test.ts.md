# NodeMapper.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/infrastructure/NodeMapper.test.ts`
- **Extension:** `.ts`
- **Size:** 750 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts.md|packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { describe, expect, it } from "vitest";
import { NodeMapper } from "./NodeMapper.ts";

describe("NodeMapper", () => {
  it("projects NodeInfo onto the Node domain shape", () => {
    const proto = create(Protobuf.Mesh.NodeInfoSchema, {
      num: 0xdeadbeef,
      lastHeard: 1700000000,
      snr: 7,
      isFavorite: true,
      isIgnored: false,
    });
    const node = NodeMapper.fromProto(proto);
    expect(node.num).toBe(0xdeadbeef);
    expect(node.lastHeard).toBe(1700000000);
    expect(node.snr).toBe(7);
    expect(node.isFavorite).toBe(true);
    expect(node.isIgnored).toBe(false);
...
```