# Message.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/domain/Message.test.ts`
- **Extension:** `.ts`
- **Size:** 859 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { MessageMapper } from "../infrastructure/MessageMapper.ts";
import { MessageState } from "./MessageState.ts";
import { ChannelNumber } from "../../../core/types.ts";

describe("MessageMapper", () => {
  it("projects a text PacketMetadata into the Message domain shape", () => {
    const now = new Date(1_700_000_000_000);
    const message = MessageMapper.fromPacket(
      {
        id: 1,
        from: 10,
        to: 20,
        channel: ChannelNumber.Primary,
        rxTime: now,
        type: "direct",
        data: "hello",
      },
      MessageState.Pending,
    );
...
```