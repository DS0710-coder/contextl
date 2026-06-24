# channelsStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/state/channelsStore.ts`
- **Extension:** `.ts`
- **Size:** 185 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChannelsStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/channels/domain/Channel.ts.md|packages/sdk/src/features/channels/domain/Channel.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { Channel } from "../domain/Channel.ts";

export class ChannelsStore extends SignalMap<number, Channel> {}
```