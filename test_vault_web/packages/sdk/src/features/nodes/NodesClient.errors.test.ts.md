# NodesClient.errors.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/NodesClient.errors.test.ts`
- **Extension:** `.ts`
- **Size:** 3739 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `nodeInfo`

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

const KEY_A = new Uint8Array([1, 2, 3, 4]);
const KEY_B = new Uint8Array([9, 8, 7, 6]);

function nodeInfo(num: number, key?: Uint8Array, longName = `Node ${num}`) {
  return create(Protobuf.Mesh.NodeInfoSchema, {
    num,
    user: create(Protobuf.Mesh.UserSchema, {
      id: `!${num.toString(16)}`,
      longName,
      shortName: longName.slice(0, 4),
      publicKey: key ?? new Uint8Array(),
    }),
  });
...
```