# ChannelUseCases.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/channels/application/ChannelUseCases.ts`
- **Extension:** `.ts`
- **Size:** 1340 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
import * as Protobuf from "@meshtastic/protobufs";
import { create } from "@bufbuild/protobuf";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { sendAdminMessage } from "../../device/infrastructure/AdminMessageSender.ts";

export async function setChannel(
  client: MeshClient,
  channel: Protobuf.Channel.Channel,
): Promise<ResultType<number, Error>> {
  try {
    const id = await sendAdminMessage(client, {
      case: "setChannel",
      value: channel,
    });
    return Result.ok(id);
  } catch (e) {
    return Result.err(e instanceof Error ? e : new Error(String(e)));
  }
...
```