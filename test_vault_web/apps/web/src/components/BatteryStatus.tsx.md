# BatteryStatus.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/BatteryStatus.tsx`
- **Extension:** `.tsx`
- **Size:** 2271 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BatteryStatusKey`
- `BatteryStatusProps`
- `StatusConfig`

## Imports (Dependencies)
- [[apps/web/src/components/types.ts.md|apps/web/src/components/types.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]

## Source Code Snippet
```tsx
import {
  BatteryFullIcon,
  BatteryLowIcon,
  BatteryMediumIcon,
  PlugZapIcon,
} from "lucide-react";
import type React from "react";
import { useTranslation } from "react-i18next";
import type { DeviceMetrics } from "./types.ts";

type BatteryStatusKey = keyof typeof BATTERY_STATUS;

interface BatteryStatusProps {
  deviceMetrics?: DeviceMetrics | null;
}

interface StatusConfig {
  Icon: React.ElementType;
  className: string;
  text: string;
...
```