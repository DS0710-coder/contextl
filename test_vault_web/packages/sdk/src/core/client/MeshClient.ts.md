# MeshClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/client/MeshClient.ts`
- **Extension:** `.ts`
- **Size:** 12008 bytes
- **Centrality Score:** 0.0213
- **In-Degree (Imported By):** 45
- **Out-Degree (Imports):** 22

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Destination`
- `PacketMetadata`
- `MeshClientOptions`
- `ConnectionProgressCounters`
- `ConnectionProgress`
- `MeshClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/constants/index.ts.md|packages/sdk/src/core/constants/index.ts]]
- [[packages/sdk/src/core/errors/MeshError.ts.md|packages/sdk/src/core/errors/MeshError.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/identifiers/PacketId.ts.md|packages/sdk/src/core/identifiers/PacketId.ts]]
- [[packages/sdk/src/core/logging/logger.ts.md|packages/sdk/src/core/logging/logger.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/core/xmodem/Xmodem.ts.md|packages/sdk/src/core/xmodem/Xmodem.ts]]
- [[packages/sdk/src/features/channels/index.ts.md|packages/sdk/src/features/channels/index.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]
- [[packages/sdk/src/features/device/index.ts.md|packages/sdk/src/features/device/index.ts]]
- [[packages/sdk/src/features/files/index.ts.md|packages/sdk/src/features/files/index.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/position/index.ts.md|packages/sdk/src/features/position/index.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]
- [[packages/sdk/src/features/traceroute/index.ts.md|packages/sdk/src/features/traceroute/index.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.progress.test.ts.md|packages/sdk/src/core/client/MeshClient.progress.test.ts]]
- [[packages/sdk/src/core/client/index.ts.md|packages/sdk/src/core/client/index.ts]]
- [[packages/sdk/src/core/registry/MeshRegistry.ts.md|packages/sdk/src/core/registry/MeshRegistry.ts]]
- [[packages/sdk/src/features/channels/ChannelsClient.test.ts.md|packages/sdk/src/features/channels/ChannelsClient.test.ts]]
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/channels/application/ChannelUseCases.ts.md|packages/sdk/src/features/channels/application/ChannelUseCases.ts]]
- [[packages/sdk/src/features/chat/ChatClient.drafts.test.ts.md|packages/sdk/src/features/chat/ChatClient.drafts.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.send.test.ts.md|packages/sdk/src/features/chat/ChatClient.send.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/ChatClient.unread.test.ts.md|packages/sdk/src/features/chat/ChatClient.unread.test.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.test.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.test.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]
- [[packages/sdk/src/features/chat/application/SendWaypointUseCase.ts.md|packages/sdk/src/features/chat/application/SendWaypointUseCase.ts]]
- [[packages/sdk/src/features/config/ConfigClient.test.ts.md|packages/sdk/src/features/config/ConfigClient.test.ts]]
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/ConfigEditor.test.ts.md|packages/sdk/src/features/config/ConfigEditor.test.ts]]
- [[packages/sdk/src/features/config/application/ConfigUseCases.ts.md|packages/sdk/src/features/config/application/ConfigUseCases.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]
- [[packages/sdk/src/features/device/application/ConfigureUseCase.ts.md|packages/sdk/src/features/device/application/ConfigureUseCase.ts]]
- [[packages/sdk/src/features/device/application/DisconnectUseCase.ts.md|packages/sdk/src/features/device/application/DisconnectUseCase.ts]]
- [[packages/sdk/src/features/device/application/GetMetadataUseCase.ts.md|packages/sdk/src/features/device/application/GetMetadataUseCase.ts]]
- [[packages/sdk/src/features/device/application/HeartbeatService.ts.md|packages/sdk/src/features/device/application/HeartbeatService.ts]]
- [[packages/sdk/src/features/device/application/RebootService.ts.md|packages/sdk/src/features/device/application/RebootService.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.errors.test.ts.md|packages/sdk/src/features/nodes/NodesClient.errors.test.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.test.ts.md|packages/sdk/src/features/nodes/NodesClient.test.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts.md|packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts]]
- [[packages/sdk/src/features/position/PositionClient.test.ts.md|packages/sdk/src/features/position/PositionClient.test.ts]]
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]
- [[packages/sdk/src/features/position/application/PositionUseCases.ts.md|packages/sdk/src/features/position/application/PositionUseCases.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/traceroute/TraceRouteClient.ts.md|packages/sdk/src/features/traceroute/TraceRouteClient.ts]]
- [[packages/sdk/src/features/traceroute/application/TraceRouteUseCase.ts.md|packages/sdk/src/features/traceroute/application/TraceRouteUseCase.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]
- [[packages/sdk/tests/integration/fake-transport.test.ts.md|packages/sdk/tests/integration/fake-transport.test.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { Logger } from "tslog";
import { Constants } from "../constants/index.ts";
import { EventBus } from "../event-bus/EventBus.ts";
import { PacketTooLargeError } from "../errors/MeshError.ts";
import { generatePacketId } from "../identifiers/PacketId.ts";
import { createLogger } from "../logging/logger.ts";
import { decodePacket } from "../packet-codec/decodePacket.ts";
import { Queue } from "../queue/Queue.ts";
import { createStore, type ReadonlySignal } from "../signals/createStore.ts";
import type { Transport } from "../transport/Transport.ts";
import { DeviceStatusEnum } from "../transport/Transport.ts";
import {
  ChannelNumber,
  type Destination,
  Emitter,
  type PacketMetadata,
} from "../types.ts";
import { Xmodem } from "../xmodem/Xmodem.ts";
...
```