# useChatAsLegacyMessages.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useChatAsLegacyMessages.ts`
- **Extension:** `.ts`
- **Size:** 2326 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Message`
- `UseChatAsLegacyMessagesBroadcast`
- `UseChatAsLegacyMessagesDirect`
- `UseChatAsLegacyMessagesParams`
- `useChatAsLegacyMessages`
- `toLegacy`
- `mapState`

## Imports (Dependencies)
- [[apps/web/src/core/stores/messageStore/index.ts.md|apps/web/src/core/stores/messageStore/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]

## Source Code Snippet
```ts
import {
  type Message as LegacyMessage,
  MessageState as LegacyMessageState,
  MessageType,
} from "@core/stores/messageStore";
import type { Message as SdkMessage } from "@meshtastic/sdk";
import { MessageState as SdkMessageState, type Types } from "@meshtastic/sdk";
import { useChat, useDirectChat } from "@meshtastic/sdk-react";
import { useMemo } from "react";

/**
 * Adapter that surfaces SDK-managed chat history in the shape expected by
 * the pre-SDK message components (`Message` from `messageStore`). Lets
 * MessagesPage / ChannelChat / MessageItem keep their current props while
 * reading from the OPFS-backed SQLite repository through the SDK chat
 * slice. Removed once those components consume `Message` from the SDK
 * directly.
 */
export interface UseChatAsLegacyMessagesBroadcast {
  type: MessageType.Broadcast;
...
```