# ChannelMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts`
- **Extension:** `.ts`
- **Size:** 272 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/channels/domain/Channel.ts.md|packages/sdk/src/features/channels/domain/Channel.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/channels/index.ts.md|packages/sdk/src/features/channels/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { Channel } from "../domain/Channel.ts";

export const ChannelMapper = {
  fromProto(ch: Protobuf.Channel.Channel): Channel {
    return { index: ch.index, role: ch.role, settings: ch.settings };
  },
};
```