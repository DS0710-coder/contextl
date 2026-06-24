# ModuleConfig.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Settings/ModuleConfig.tsx`
- **Extension:** `.tsx`
- **Size:** 5517 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 20

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConfigProps`
- `TabItem`

## Imports (Dependencies)
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
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/components/UI/Tabs.tsx.md|apps/web/src/components/UI/Tabs.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { AmbientLighting } from "@components/PageComponents/ModuleConfig/AmbientLighting.tsx";
import { Audio } from "@components/PageComponents/ModuleConfig/Audio.tsx";
import { CannedMessage } from "@components/PageComponents/ModuleConfig/CannedMessage.tsx";
import { DetectionSensor } from "@components/PageComponents/ModuleConfig/DetectionSensor.tsx";
import { ExternalNotification } from "@components/PageComponents/ModuleConfig/ExternalNotification.tsx";
import { MQTT } from "@components/PageComponents/ModuleConfig/MQTT.tsx";
import { NeighborInfo } from "@components/PageComponents/ModuleConfig/NeighborInfo.tsx";
import { Paxcounter } from "@components/PageComponents/ModuleConfig/Paxcounter.tsx";
import { RangeTest } from "@components/PageComponents/ModuleConfig/RangeTest.tsx";
import { RemoteHardware } from "@components/PageComponents/ModuleConfig/RemoteHardware.tsx";
import { Serial } from "@components/PageComponents/ModuleConfig/Serial.tsx";
import { StatusMessage } from "@components/PageComponents/ModuleConfig/StatusMessage.tsx";
import { StoreForward } from "@components/PageComponents/ModuleConfig/StoreForward.tsx";
import { Tak } from "@components/PageComponents/ModuleConfig/Tak.tsx";
import { Telemetry } from "@components/PageComponents/ModuleConfig/Telemetry.tsx";
import { TrafficManagement } from "@components/PageComponents/ModuleConfig/TrafficManagement.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import {
  Tabs,
  TabsContent,
...
```