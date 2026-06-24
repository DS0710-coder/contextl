# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/messageStore/index.ts`
- **Extension:** `.ts`
- **Size:** 1180 bytes
- **Centrality Score:** 0.0033
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
Legacy enums and message-shape types preserved for components that still
read from the SDK chat slice via the `useChatAsLegacyMessages` adapter. The Zustand
messageStore that previously lived here has been retired — chat
persistence is owned by the SDK ChatClient + SqlocalMessageRepository.

## Structural Outline
- `NodeNum`
- `MessageId`
- `ChannelId`
- `ConversationId`
- `MessageBase`
- `GenericMessage`
- `Message`
- `getConversationId`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Messages/ChannelChat.tsx.md|apps/web/src/components/PageComponents/Messages/ChannelChat.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/core/hooks/useChatAsLegacyMessages.ts.md|apps/web/src/core/hooks/useChatAsLegacyMessages.ts]]
- [[apps/web/src/core/hooks/useChatLegacy.ts.md|apps/web/src/core/hooks/useChatLegacy.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Source Code Snippet
```ts
/**
 * Legacy enums and message-shape types preserved for components that still
 * read from the SDK chat slice via the `useChatAsLegacyMessages` adapter. The Zustand
 * messageStore that previously lived here has been retired — chat
 * persistence is owned by the SDK ChatClient + SqlocalMessageRepository.
 */

import type { Types } from "@meshtastic/sdk";

export enum MessageState {
  Ack = "ack",
  Waiting = "waiting",
  Failed = "failed",
}

export enum MessageType {
  Direct = "direct",
  Broadcast = "broadcast",
}

...
```