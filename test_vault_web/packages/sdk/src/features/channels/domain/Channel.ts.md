# Channel.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/domain/Channel.ts`
- **Extension:** `.ts`
- **Size:** 216 bytes
- **Centrality Score:** 0.0045
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Channel`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/channels/index.ts.md|packages/sdk/src/features/channels/index.ts]]
- [[packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts.md|packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts]]
- [[packages/sdk/src/features/channels/state/channelsStore.ts.md|packages/sdk/src/features/channels/state/channelsStore.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

export interface Channel {
  readonly index: number;
  readonly role: Protobuf.Channel.Channel_Role;
  readonly settings?: Protobuf.Channel.ChannelSettings;
}
```