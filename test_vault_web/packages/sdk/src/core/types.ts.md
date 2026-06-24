# types.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/types.ts`
- **Extension:** `.ts`
- **Size:** 1961 bytes
- **Centrality Score:** 0.0234
- **In-Degree (Imported By):** 31
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `QueueItem`
- `LogEventPacket`
- `PacketDestination`
- `PacketMetadata`
- `LogEvent`
- `Destination`
- `PacketError`

## Imports (Dependencies)
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/features/chat/ChatClient.drafts.test.ts.md|packages/sdk/src/features/chat/ChatClient.drafts.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.send.test.ts.md|packages/sdk/src/features/chat/ChatClient.send.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/ChatClient.unread.test.ts.md|packages/sdk/src/features/chat/ChatClient.unread.test.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]
- [[packages/sdk/src/features/chat/application/SendWaypointUseCase.ts.md|packages/sdk/src/features/chat/application/SendWaypointUseCase.ts]]
- [[packages/sdk/src/features/chat/domain/Message.test.ts.md|packages/sdk/src/features/chat/domain/Message.test.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.test.ts]]
- [[packages/sdk/src/features/chat/state/chatStore.ts.md|packages/sdk/src/features/chat/state/chatStore.ts]]
- [[packages/sdk/src/features/device/application/GetMetadataUseCase.ts.md|packages/sdk/src/features/device/application/GetMetadataUseCase.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.errors.test.ts.md|packages/sdk/src/features/nodes/NodesClient.errors.test.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.test.ts.md|packages/sdk/src/features/nodes/NodesClient.test.ts]]
- [[packages/sdk/src/features/position/PositionClient.test.ts.md|packages/sdk/src/features/position/PositionClient.test.ts]]
- [[packages/sdk/src/features/position/infrastructure/PositionMapper.ts.md|packages/sdk/src/features/position/infrastructure/PositionMapper.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.test.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts.md|packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]
- [[packages/sdk/src/shim/legacyTypes.ts.md|packages/sdk/src/shim/legacyTypes.ts]]
- [[packages/sdk/src/types-namespace.ts.md|packages/sdk/src/types-namespace.ts]]
- [[packages/sdk/tests/integration/fake-transport.test.ts.md|packages/sdk/tests/integration/fake-transport.test.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

export type {
  DeviceOutput,
  HttpRetryConfig,
  Transport,
} from "./transport/Transport.ts";
export { DeviceStatusEnum } from "./transport/Transport.ts";

export interface QueueItem {
  id: number;
  data: Uint8Array;
  sent: boolean;
  added: Date;
  promise: Promise<number>;
}

export type LogEventPacket = LogEvent & { date: Date };

export type PacketDestination = "broadcast" | "direct";
...
```