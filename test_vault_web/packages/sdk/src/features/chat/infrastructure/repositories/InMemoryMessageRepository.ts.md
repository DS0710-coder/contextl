# InMemoryMessageRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts`
- **Extension:** `.ts`
- **Size:** 2890 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConversationKey`
- `MessageRepository`
- `RetentionPolicy`
- `InMemoryMessageRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts]]

## Source Code Snippet
```ts
import type { Message } from "../../domain/Message.ts";
import type { MessageState } from "../../domain/MessageState.ts";
import {
  type ConversationKey,
  conversationKeyString,
  type MessageRepository,
  type RetentionPolicy,
} from "../../domain/MessageRepository.ts";

/**
 * Default in-memory MessageRepository. No persistence across reloads; useful
 * for tests and for single-session apps that do not need history.
 */
export class InMemoryMessageRepository implements MessageRepository {
  private readonly buckets = new Map<string, Message[]>();

  async loadRecent(key: ConversationKey, limit: number): Promise<Message[]> {
    const bucket = this.buckets.get(conversationKeyString(key)) ?? [];
    return bucket.slice(-limit);
  }
...
```