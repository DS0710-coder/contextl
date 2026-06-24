# MessageMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/infrastructure/MessageMapper.ts`
- **Extension:** `.ts`
- **Size:** 532 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/domain/Message.test.ts.md|packages/sdk/src/features/chat/domain/Message.test.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]

## Source Code Snippet
```ts
import type { PacketMetadata } from "../../../core/types.ts";
import type { Message } from "../domain/Message.ts";
import { MessageState } from "../domain/MessageState.ts";

export const MessageMapper = {
  fromPacket(
    packet: PacketMetadata<string>,
    state: MessageState = MessageState.Ack,
  ): Message {
    return {
      id: packet.id,
      from: packet.from,
      to: packet.to,
      channel: packet.channel,
      rxTime: packet.rxTime,
      type: packet.type,
      text: packet.data,
      state,
    };
  },
...
```