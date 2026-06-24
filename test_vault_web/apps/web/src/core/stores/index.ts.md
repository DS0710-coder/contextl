# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/index.ts`
- **Extension:** `.ts`
- **Size:** 1493 bytes
- **Centrality Score:** 0.0152
- **In-Degree (Imported By):** 68
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceContext`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useDeviceContext.ts.md|apps/web/src/core/hooks/useDeviceContext.ts]]
- [[apps/web/src/core/stores/appStore/index.ts.md|apps/web/src/core/stores/appStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/selectors.ts.md|apps/web/src/core/stores/deviceStore/selectors.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/stores/messageStore/index.ts.md|apps/web/src/core/stores/messageStore/index.ts]]
- [[apps/web/src/core/stores/sidebarStore/index.tsx.md|apps/web/src/core/stores/sidebarStore/index.tsx]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/DeviceWrapper.tsx.md|apps/web/src/DeviceWrapper.tsx]]
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx.md|apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx]]
- [[apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx.md|apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx]]
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/PKIBackupDialog.tsx.md|apps/web/src/components/Dialog/PKIBackupDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts.md|apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts]]
- [[apps/web/src/components/Dialog/RemoveNodeDialog.tsx.md|apps/web/src/components/Dialog/RemoveNodeDialog.tsx]]
- [[apps/web/src/components/Dialog/ShutdownDialog.tsx.md|apps/web/src/components/Dialog/ShutdownDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts.md|apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts]]
- [[apps/web/src/components/KeyBackupReminder.tsx.md|apps/web/src/components/KeyBackupReminder.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx.md|apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Bluetooth.tsx.md|apps/web/src/components/PageComponents/Settings/Bluetooth.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Display.tsx.md|apps/web/src/components/PageComponents/Settings/Display.tsx]]
- [[apps/web/src/components/PageComponents/Settings/LoRa.tsx.md|apps/web/src/components/PageComponents/Settings/LoRa.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Power.tsx.md|apps/web/src/components/PageComponents/Settings/Power.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarButton.tsx.md|apps/web/src/components/UI/Sidebar/SidebarButton.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarSection.tsx.md|apps/web/src/components/UI/Sidebar/SidebarSection.tsx]]
- [[apps/web/src/core/dto/PacketToMessageDTO.ts.md|apps/web/src/core/dto/PacketToMessageDTO.ts]]
- [[apps/web/src/core/hooks/useNewNodeNum.ts.md|apps/web/src/core/hooks/useNewNodeNum.ts]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/messageStore/types.ts.md|apps/web/src/core/stores/messageStore/types.ts]]
- [[apps/web/src/core/subscriptions.ts.md|apps/web/src/core/subscriptions.ts]]
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]
- [[apps/web/src/sdk-preview/react/useConfigEditor.ts.md|apps/web/src/sdk-preview/react/useConfigEditor.ts]]

## Source Code Snippet
```ts
import { useDeviceContext } from "@core/hooks/useDeviceContext.ts";
import { type Device, useDeviceStore } from "@core/stores/deviceStore/index.ts";

export {
  CurrentDeviceContext,
  type DeviceContext,
  useDeviceContext,
} from "@core/hooks/useDeviceContext";
export { useAppStore } from "@core/stores/appStore/index.ts";
export { type Device, useDeviceStore } from "@core/stores/deviceStore/index.ts";
export {
  useActiveConnection,
  useActiveConnectionId,
  useAddSavedConnection,
  useConnectionError,
  useConnectionForDevice,
  useConnectionStatus,
  useDefaultConnection,
  useDeviceForConnection,
  useFirstSavedConnection,
...
```