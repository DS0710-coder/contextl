# MessageState.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/domain/MessageState.ts`
- **Extension:** `.ts`
- **Size:** 88 bytes
- **Centrality Score:** 0.0057
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.send.test.ts.md|packages/sdk/src/features/chat/ChatClient.send.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/domain/Message.test.ts.md|packages/sdk/src/features/chat/domain/Message.test.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]
- [[packages/sdk/src/features/chat/state/chatStore.ts.md|packages/sdk/src/features/chat/state/chatStore.ts]]

## Source Code Snippet
```ts
export enum MessageState {
  Pending = "pending",
  Ack = "ack",
  Failed = "failed",
}
```