# ChannelsClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/ChannelsClient.ts`
- **Extension:** `.ts`
- **Size:** 1435 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChannelsClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/channels/application/ChannelUseCases.ts.md|packages/sdk/src/features/channels/application/ChannelUseCases.ts]]
- [[packages/sdk/src/features/channels/domain/Channel.ts.md|packages/sdk/src/features/channels/domain/Channel.ts]]
- [[packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts.md|packages/sdk/src/features/channels/infrastructure/ChannelMapper.ts]]
- [[packages/sdk/src/features/channels/state/channelsStore.ts.md|packages/sdk/src/features/channels/state/channelsStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/index.ts.md|packages/sdk/src/features/channels/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import {
  clearChannel,
  getChannel,
  setChannel,
} from "./application/ChannelUseCases.ts";
import type { Channel } from "./domain/Channel.ts";
import { ChannelMapper } from "./infrastructure/ChannelMapper.ts";
import { ChannelsStore } from "./state/channelsStore.ts";

export class ChannelsClient {
  private readonly client: MeshClient;
  private readonly store: ChannelsStore;
  public readonly list: ReadonlySignal<ReadonlyArray<Channel>>;

  constructor(client: MeshClient) {
    this.client = client;
...
```