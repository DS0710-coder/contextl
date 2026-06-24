# AdminMessageSender.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts`
- **Extension:** `.ts`
- **Size:** 1020 bytes
- **Centrality Score:** 0.0049
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `sendAdminMessage`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/channels/application/ChannelUseCases.ts.md|packages/sdk/src/features/channels/application/ChannelUseCases.ts]]
- [[packages/sdk/src/features/config/application/ConfigUseCases.ts.md|packages/sdk/src/features/config/application/ConfigUseCases.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/device/application/GetMetadataUseCase.ts.md|packages/sdk/src/features/device/application/GetMetadataUseCase.ts]]
- [[packages/sdk/src/features/device/application/RebootService.ts.md|packages/sdk/src/features/device/application/RebootService.ts]]
- [[packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts.md|packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts]]
- [[packages/sdk/src/features/position/application/PositionUseCases.ts.md|packages/sdk/src/features/position/application/PositionUseCases.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { ChannelNumber, type Destination } from "../../../core/types.ts";

/**
 * Builds an AdminMessage from a payload variant and sends it over the ADMIN_APP
 * portnum. Shared by config, channels, nodes, position, and device slices so
 * the plumbing is not duplicated across 15+ use-cases.
 */
export function sendAdminMessage(
  client: MeshClient,
  payloadVariant: Protobuf.Admin.AdminMessage["payloadVariant"],
  destination: Destination = "self",
  channel: ChannelNumber = ChannelNumber.Primary,
  wantAck = true,
  wantResponse = true,
): Promise<number> {
  const message = create(Protobuf.Admin.AdminMessageSchema, { payloadVariant });
  return client.sendPacket(
...
```