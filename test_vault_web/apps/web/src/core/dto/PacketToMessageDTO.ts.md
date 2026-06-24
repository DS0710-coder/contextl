# PacketToMessageDTO.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/dto/PacketToMessageDTO.ts`
- **Extension:** `.ts`
- **Size:** 1545 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PacketToMessageDTO`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/stores/messageStore/types.ts.md|apps/web/src/core/stores/messageStore/types.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { MessageState, MessageType } from "@core/stores";
import type { Message } from "@core/stores/messageStore/types.ts";
import type { Types } from "@meshtastic/sdk";

class PacketToMessageDTO {
  channel: Types.ChannelNumber;
  to: number;
  from: number;
  date: number; // (timestamp ms)
  messageId: number;
  state: MessageState;
  message: string;
  type: MessageType;

  constructor(data: Types.PacketMetadata<string>, nodeNum: number) {
    this.channel = data.channel;
    this.to = data.to;
    this.from = data.from;
    this.messageId = data.id;
    this.state =
...
```