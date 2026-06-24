# DeviceInfoPanel.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/DeviceInfoPanel.tsx`
- **Extension:** `.tsx`
- **Size:** 9075 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LucideIcon`
- `DeviceInfoPanelProps`
- `InfoDisplayItem`
- `ActionButtonConfig`

## Imports (Dependencies)
- [[apps/web/src/components/BatteryStatus.tsx.md|apps/web/src/components/BatteryStatus.tsx]]
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/components/ThemeSwitcher.tsx.md|apps/web/src/components/ThemeSwitcher.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]
- [[apps/web/src/components/types.ts.md|apps/web/src/components/types.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]

## Source Code Snippet
```tsx
import type { ConnectionStatus } from "@app/core/stores/deviceStore/types.ts";
import { cn } from "@core/utils/cn.ts";
import type { Protobuf } from "@meshtastic/sdk";
import { useNavigate } from "@tanstack/react-router";
import {
  ChevronRight,
  CpuIcon,
  Languages,
  type LucideIcon,
  Palette,
  Search as SearchIcon,
  ZapIcon,
} from "lucide-react";
import type React from "react";
import { Fragment } from "react";
import { useTranslation } from "react-i18next";
import BatteryStatus from "./BatteryStatus.tsx";
import LanguageSwitcher from "./LanguageSwitcher.tsx";
import ThemeSwitcher from "./ThemeSwitcher.tsx";
import type { DeviceMetrics } from "./types.ts";
...
```