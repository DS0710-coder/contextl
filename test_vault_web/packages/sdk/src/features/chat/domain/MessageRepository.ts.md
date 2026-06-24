# MessageRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/domain/MessageRepository.ts`
- **Extension:** `.ts`
- **Size:** 1686 bytes
- **Centrality Score:** 0.0042
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConversationKey`
- `RetentionPolicy`
- `MessageRepository`
- `conversationKeyString`

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/domain/DraftRepository.ts.md|packages/sdk/src/features/chat/domain/DraftRepository.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]
- [[packages/sdk/src/features/chat/state/draftStore.ts.md|packages/sdk/src/features/chat/state/draftStore.ts]]

## Source Code Snippet
```ts
import type { ChannelNumber } from "../../../core/types.ts";
import type { Message } from "./Message.ts";
import type { MessageState } from "./MessageState.ts";

/**
 * Conversation key. Broadcast messages are keyed by channel; direct messages
 * are keyed by the peer node number.
 */
export type ConversationKey =
  | { kind: "channel"; channel: ChannelNumber }
  | { kind: "direct"; peer: number };

export interface RetentionPolicy {
  /** Drop anything older than this many ms. */
  olderThanMs?: number;
  /** Keep at most this many messages per conversation. */
  maxPerBucket?: number;
}

/**
...
```