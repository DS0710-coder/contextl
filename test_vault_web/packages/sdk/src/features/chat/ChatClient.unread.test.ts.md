# ChatClient.unread.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/ChatClient.unread.test.ts`
- **Extension:** `.ts`
- **Size:** 2922 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `dispatchInbound`
- `setMyNode`

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

const MY_NODE = 0xdeadbeef;

function dispatchInbound(
  client: MeshClient,
  opts: {
    from: number;
    to?: number;
    channel?: ChannelNumber;
    type?: "direct" | "broadcast";
    ms: number;
    text?: string;
  },
): void {
...
```