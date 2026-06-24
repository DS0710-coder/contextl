# ChatClient.persistence.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/ChatClient.persistence.test.ts`
- **Extension:** `.ts`
- **Size:** 2996 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `seedMessage`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../core/types.ts";
import { InMemoryMessageRepository } from "./infrastructure/repositories/InMemoryMessageRepository.ts";
import type { Message } from "./domain/Message.ts";
import { MessageState } from "./domain/MessageState.ts";

function seedMessage(id: number, ms: number, text: string): Message {
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
...
```