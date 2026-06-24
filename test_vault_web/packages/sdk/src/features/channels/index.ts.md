# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/index.ts`
- **Extension:** `.ts`
- **Size:** 173 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/channels/domain/Channel.ts.md|packages/sdk/src/features/channels/domain/Channel.ts]]
- [[packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts.md|packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { ChannelsClient } from "./ChannelsClient.ts";
export type { Channel } from "./domain/Channel.ts";
export { ChannelMapper } from "./infrastructure/ChannelMapper.ts";
```