# mod.ts

## Architecture Metrics
- **Path:** `packages/sdk/mod.ts`
- **Extension:** `.ts`
- **Size:** 4448 bytes
- **Centrality Score:** 0.0713
- **In-Degree (Imported By):** 130
- **Out-Degree (Imports):** 24

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/constants/index.ts.md|packages/sdk/src/core/constants/index.ts]]
- [[packages/sdk/src/core/errors/MeshError.ts.md|packages/sdk/src/core/errors/MeshError.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/identifiers/PacketId.ts.md|packages/sdk/src/core/identifiers/PacketId.ts]]
- [[packages/sdk/src/core/logging/logger.ts.md|packages/sdk/src/core/logging/logger.ts]]
- [[packages/sdk/src/core/packet-codec/fromDevice.ts.md|packages/sdk/src/core/packet-codec/fromDevice.ts]]
- [[packages/sdk/src/core/packet-codec/toDevice.ts.md|packages/sdk/src/core/packet-codec/toDevice.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/core/registry/MeshRegistry.ts.md|packages/sdk/src/core/registry/MeshRegistry.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/core/xmodem/Xmodem.ts.md|packages/sdk/src/core/xmodem/Xmodem.ts]]
- [[packages/sdk/src/features/channels/index.ts.md|packages/sdk/src/features/channels/index.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]
- [[packages/sdk/src/features/device/index.ts.md|packages/sdk/src/features/device/index.ts]]
- [[packages/sdk/src/features/files/index.ts.md|packages/sdk/src/features/files/index.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/position/index.ts.md|packages/sdk/src/features/position/index.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]
- [[packages/sdk/src/features/traceroute/index.ts.md|packages/sdk/src/features/traceroute/index.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/LocationResponseDialog.tsx.md|apps/web/src/components/Dialog/LocationResponseDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx]]
- [[apps/web/src/components/Dialog/TracerouteResponseDialog.tsx.md|apps/web/src/components/Dialog/TracerouteResponseDialog.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/components/PageComponents/Map/cluster.ts.md|apps/web/src/components/PageComponents/Map/cluster.ts]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.test.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.test.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx]]
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Bluetooth.tsx.md|apps/web/src/components/PageComponents/Settings/Bluetooth.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Display.tsx.md|apps/web/src/components/PageComponents/Settings/Display.tsx]]
- [[apps/web/src/components/PageComponents/Settings/LoRa.tsx.md|apps/web/src/components/PageComponents/Settings/LoRa.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Power.tsx.md|apps/web/src/components/PageComponents/Settings/Power.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]
- [[apps/web/src/components/PageComponents/Settings/User.tsx.md|apps/web/src/components/PageComponents/Settings/User.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.test.ts.md|apps/web/src/components/generic/Filter/useFilterNode.test.ts]]
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[apps/web/src/core/connections/heartbeat.ts.md|apps/web/src/core/connections/heartbeat.ts]]
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]
- [[apps/web/src/core/dto/NodeNumToNodeInfoDTO.ts.md|apps/web/src/core/dto/NodeNumToNodeInfoDTO.ts]]
- [[apps/web/src/core/dto/PacketToMessageDTO.ts.md|apps/web/src/core/dto/PacketToMessageDTO.ts]]
- [[apps/web/src/core/hooks/useChatAsLegacyMessages.ts.md|apps/web/src/core/hooks/useChatAsLegacyMessages.ts]]
- [[apps/web/src/core/hooks/useChatLegacy.ts.md|apps/web/src/core/hooks/useChatLegacy.ts]]
- [[apps/web/src/core/hooks/useMapFitting.ts.md|apps/web/src/core/hooks/useMapFitting.ts]]
- [[apps/web/src/core/hooks/useNewNodeNum.ts.md|apps/web/src/core/hooks/useNewNodeNum.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/useNodesLegacy.ts.md|apps/web/src/core/hooks/useNodesLegacy.ts]]
- [[apps/web/src/core/meshRegistry.ts.md|apps/web/src/core/meshRegistry.ts]]
- [[apps/web/src/core/sdkStorage.ts.md|apps/web/src/core/sdkStorage.ts]]
- [[apps/web/src/core/stores/deviceStore/deviceStore.mock.ts.md|apps/web/src/core/stores/deviceStore/deviceStore.mock.ts]]
- [[apps/web/src/core/stores/deviceStore/deviceStore.test.ts.md|apps/web/src/core/stores/deviceStore/deviceStore.test.ts]]
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/stores/messageStore/index.ts.md|apps/web/src/core/stores/messageStore/index.ts]]
- [[apps/web/src/core/stores/messageStore/types.ts.md|apps/web/src/core/stores/messageStore/types.ts]]
- [[apps/web/src/core/subscriptions.ts.md|apps/web/src/core/subscriptions.ts]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/validation/channel.ts.md|apps/web/src/validation/channel.ts]]
- [[apps/web/src/validation/config/bluetooth.ts.md|apps/web/src/validation/config/bluetooth.ts]]
- [[apps/web/src/validation/config/device.ts.md|apps/web/src/validation/config/device.ts]]
- [[apps/web/src/validation/config/display.ts.md|apps/web/src/validation/config/display.ts]]
- [[apps/web/src/validation/config/lora.test.ts.md|apps/web/src/validation/config/lora.test.ts]]
- [[apps/web/src/validation/config/lora.ts.md|apps/web/src/validation/config/lora.ts]]
- [[apps/web/src/validation/config/network.ts.md|apps/web/src/validation/config/network.ts]]
- [[apps/web/src/validation/config/position.ts.md|apps/web/src/validation/config/position.ts]]
- [[apps/web/src/validation/moduleConfig/audio.ts.md|apps/web/src/validation/moduleConfig/audio.ts]]
- [[apps/web/src/validation/moduleConfig/cannedMessage.ts.md|apps/web/src/validation/moduleConfig/cannedMessage.ts]]
- [[apps/web/src/validation/moduleConfig/detectionSensor.ts.md|apps/web/src/validation/moduleConfig/detectionSensor.ts]]
- [[apps/web/src/validation/moduleConfig/serial.ts.md|apps/web/src/validation/moduleConfig/serial.ts]]
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useClientById.ts.md|packages/sdk-react/src/adapters/useClientById.ts]]
- [[packages/sdk-react/src/adapters/useMeshRegistry.ts.md|packages/sdk-react/src/adapters/useMeshRegistry.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk-react/src/adapters/useSignalValue.ts.md|packages/sdk-react/src/adapters/useSignalValue.ts]]
- [[packages/sdk-react/src/hooks/useChannels.ts.md|packages/sdk-react/src/hooks/useChannels.ts]]
- [[packages/sdk-react/src/hooks/useChat.ts.md|packages/sdk-react/src/hooks/useChat.ts]]
- [[packages/sdk-react/src/hooks/useConfig.ts.md|packages/sdk-react/src/hooks/useConfig.ts]]
- [[packages/sdk-react/src/hooks/useConfigEditor.ts.md|packages/sdk-react/src/hooks/useConfigEditor.ts]]
- [[packages/sdk-react/src/hooks/useConnection.ts.md|packages/sdk-react/src/hooks/useConnection.ts]]
- [[packages/sdk-react/src/hooks/useConnectionProgress.ts.md|packages/sdk-react/src/hooks/useConnectionProgress.ts]]
- [[packages/sdk-react/src/hooks/useDirectChat.ts.md|packages/sdk-react/src/hooks/useDirectChat.ts]]
- [[packages/sdk-react/src/hooks/useDraft.ts.md|packages/sdk-react/src/hooks/useDraft.ts]]
- [[packages/sdk-react/src/hooks/useFileTransfer.ts.md|packages/sdk-react/src/hooks/useFileTransfer.ts]]
- [[packages/sdk-react/src/hooks/useMeshDevice.ts.md|packages/sdk-react/src/hooks/useMeshDevice.ts]]
- [[packages/sdk-react/src/hooks/useNode.ts.md|packages/sdk-react/src/hooks/useNode.ts]]
- [[packages/sdk-react/src/hooks/useNodeError.ts.md|packages/sdk-react/src/hooks/useNodeError.ts]]
- [[packages/sdk-react/src/hooks/useNodes.ts.md|packages/sdk-react/src/hooks/useNodes.ts]]
- [[packages/sdk-react/src/hooks/usePosition.ts.md|packages/sdk-react/src/hooks/usePosition.ts]]
- [[packages/sdk-react/src/hooks/useTelemetry.ts.md|packages/sdk-react/src/hooks/useTelemetry.ts]]
- [[packages/sdk-react/src/hooks/useTraceroute.ts.md|packages/sdk-react/src/hooks/useTraceroute.ts]]
- [[packages/sdk-react/src/hooks/useUnread.ts.md|packages/sdk-react/src/hooks/useUnread.ts]]
- [[packages/sdk-react/src/provider/MeshContext.ts.md|packages/sdk-react/src/provider/MeshContext.ts]]
- [[packages/sdk-react/src/provider/MeshProvider.tsx.md|packages/sdk-react/src/provider/MeshProvider.tsx]]
- [[packages/sdk-react/src/provider/MeshRegistryContext.ts.md|packages/sdk-react/src/provider/MeshRegistryContext.ts]]
- [[packages/sdk-react/src/provider/MeshRegistryProvider.tsx.md|packages/sdk-react/src/provider/MeshRegistryProvider.tsx]]
- [[packages/sdk-react/tests/hooks.registry.test.tsx.md|packages/sdk-react/tests/hooks.registry.test.tsx]]
- [[packages/sdk-react/tests/hooks.test.tsx.md|packages/sdk-react/tests/hooks.test.tsx]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts]]
- [[packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts.md|packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts]]
- [[packages/transport-deno/src/transport.ts.md|packages/transport-deno/src/transport.ts]]
- [[packages/transport-http/src/transport.ts.md|packages/transport-http/src/transport.ts]]
- [[packages/transport-node-serial/src/transport.test.ts.md|packages/transport-node-serial/src/transport.test.ts]]
- [[packages/transport-node-serial/src/transport.ts.md|packages/transport-node-serial/src/transport.ts]]
- [[packages/transport-node/src/transport.test.ts.md|packages/transport-node/src/transport.test.ts]]
- [[packages/transport-node/src/transport.ts.md|packages/transport-node/src/transport.ts]]
- [[packages/transport-web-bluetooth/src/transport.ts.md|packages/transport-web-bluetooth/src/transport.ts]]
- [[packages/transport-web-serial/src/transport.test.ts.md|packages/transport-web-serial/src/transport.test.ts]]
- [[packages/transport-web-serial/src/transport.ts.md|packages/transport-web-serial/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Source Code Snippet
```ts
// Main entry
export { MeshClient } from "./src/core/client/MeshClient.ts";
export type {
  ConnectionProgress,
  ConnectionProgressCounters,
  MeshClientOptions,
} from "./src/core/client/MeshClient.ts";
export { MeshRegistry } from "./src/core/registry/MeshRegistry.ts";
export type {
  ConnectionId,
  RegistryEntry,
} from "./src/core/registry/MeshRegistry.ts";

// Constants & errors
export { Constants } from "./src/core/constants/index.ts";
export {
  MeshError,
  PacketTooLargeError,
  TransportClosedError,
} from "./src/core/errors/MeshError.ts";
...
```