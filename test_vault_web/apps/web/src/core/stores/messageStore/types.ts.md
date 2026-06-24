# types.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/messageStore/types.ts`
- **Extension:** `.ts`
- **Size:** 1616 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeNum`
- `MessageId`
- `ChannelId`
- `ConversationId`
- `MessageLogMap`
- `MessageBase`
- `GenericMessage`
- `Message`
- `GetMessagesParams`
- `SetMessageStateParams`
- `ClearMessageParams`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/dto/PacketToMessageDTO.ts.md|apps/web/src/core/dto/PacketToMessageDTO.ts]]

## Source Code Snippet
```ts
import type { MessageState, MessageType } from "@core/stores";
import type { Types } from "@meshtastic/sdk";

type NodeNum = number;
type MessageId = number;
type ChannelId = Types.ChannelNumber;
type ConversationId = string;
type MessageLogMap = Map<MessageId, Message>;

interface MessageBase {
  channel: Types.ChannelNumber;
  to: number;
  from: number;
  date: number;
  messageId: number;
  state: MessageState;
  message: string;
}

interface GenericMessage<T extends MessageType> extends MessageBase {
...
```