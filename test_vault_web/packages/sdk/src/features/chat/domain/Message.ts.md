# Message.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/domain/Message.ts`
- **Extension:** `.ts`
- **Size:** 445 bytes
- **Centrality Score:** 0.0037
- **In-Degree (Imported By):** 8
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Message`

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]
- [[packages/sdk/src/features/chat/state/chatStore.ts.md|packages/sdk/src/features/chat/state/chatStore.ts]]

## Source Code Snippet
```ts
import type { ChannelNumber, PacketDestination } from "../../../core/types.ts";
import type { MessageState } from "./MessageState.ts";

/**
 * A text message sent or received on the mesh.
 */
export interface Message {
  readonly id: number;
  readonly from: number;
  readonly to: number;
  readonly channel: ChannelNumber;
  readonly rxTime: Date;
  readonly type: PacketDestination;
  readonly text: string;
  readonly state: MessageState;
}
```