# InMemoryMessageRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 2638 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `msg`

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { ChannelNumber } from "../../../../core/types.ts";
import type { Message } from "../../domain/Message.ts";
import { MessageState } from "../../domain/MessageState.ts";
import { InMemoryMessageRepository } from "./InMemoryMessageRepository.ts";

function msg(id: number, ms: number, text = "t"): Message {
  return {
    id,
    from: 1,
    to: 0xffffffff,
    channel: ChannelNumber.Primary,
    rxTime: new Date(ms),
    type: "broadcast",
    text,
    state: MessageState.Ack,
  };
}

describe("InMemoryMessageRepository", () => {
...
```