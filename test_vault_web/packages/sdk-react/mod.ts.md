# mod.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/mod.ts`
- **Extension:** `.ts`
- **Size:** 2547 bytes
- **Centrality Score:** 0.0107
- **In-Degree (Imported By):** 52
- **Out-Degree (Imports):** 29

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
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
- [[packages/sdk-react/src/hooks/useFavoriteNode.ts.md|packages/sdk-react/src/hooks/useFavoriteNode.ts]]
- [[packages/sdk-react/src/hooks/useFileTransfer.ts.md|packages/sdk-react/src/hooks/useFileTransfer.ts]]
- [[packages/sdk-react/src/hooks/useIgnoreNode.ts.md|packages/sdk-react/src/hooks/useIgnoreNode.ts]]
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

## Imported By (Dependents)
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.test.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.test.tsx]]
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts.md|apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts]]
- [[apps/web/src/components/Dialog/RemoveNodeDialog.tsx.md|apps/web/src/components/Dialog/RemoveNodeDialog.tsx]]
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
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
- [[apps/web/src/components/RegionSetupReminder.tsx.md|apps/web/src/components/RegionSetupReminder.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/core/hooks/useChatAsLegacyMessages.ts.md|apps/web/src/core/hooks/useChatAsLegacyMessages.ts]]
- [[apps/web/src/core/hooks/useChatLegacy.ts.md|apps/web/src/core/hooks/useChatLegacy.ts]]
- [[apps/web/src/core/hooks/useFavoriteNode.ts.md|apps/web/src/core/hooks/useFavoriteNode.ts]]
- [[apps/web/src/core/hooks/useIgnoreNode.ts.md|apps/web/src/core/hooks/useIgnoreNode.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/useNodesLegacy.ts.md|apps/web/src/core/hooks/useNodesLegacy.ts]]
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]
- [[packages/sdk-react/tests/hooks.registry.test.tsx.md|packages/sdk-react/tests/hooks.registry.test.tsx]]
- [[packages/sdk-react/tests/hooks.test.tsx.md|packages/sdk-react/tests/hooks.test.tsx]]

## Source Code Snippet
```ts
export { MeshProvider } from "./src/provider/MeshProvider.tsx";
export type { MeshProviderProps } from "./src/provider/MeshProvider.tsx";
export { MeshContext } from "./src/provider/MeshContext.ts";
export { MeshRegistryProvider } from "./src/provider/MeshRegistryProvider.tsx";
export type { MeshRegistryProviderProps } from "./src/provider/MeshRegistryProvider.tsx";
export { MeshRegistryContext } from "./src/provider/MeshRegistryContext.ts";

export { useClient } from "./src/adapters/useClient.ts";
export { useClientById } from "./src/adapters/useClientById.ts";
export { useActiveClient } from "./src/adapters/useActiveClient.ts";
export {
  useMeshRegistry,
  useOptionalMeshRegistry,
} from "./src/adapters/useMeshRegistry.ts";
export { useSignal } from "./src/adapters/useSignal.ts";
export { useSignalValue } from "./src/adapters/useSignalValue.ts";

export { useMeshDevice } from "./src/hooks/useMeshDevice.ts";
export type { UseMeshDeviceResult } from "./src/hooks/useMeshDevice.ts";
export { useConnection } from "./src/hooks/useConnection.ts";
...
```