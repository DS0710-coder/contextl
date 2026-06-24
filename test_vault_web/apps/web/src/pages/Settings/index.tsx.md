# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Settings/index.tsx`
- **Extension:** `.tsx`
- **Size:** 7788 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarButton.tsx.md|apps/web/src/components/UI/Sidebar/SidebarButton.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarSection.tsx.md|apps/web/src/components/UI/Sidebar/SidebarSection.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import { deviceRoute, moduleRoute, radioRoute } from "@app/routes";
import { PageLayout } from "@components/PageLayout.tsx";
import { Sidebar } from "@components/Sidebar.tsx";
import { SidebarButton } from "@components/UI/Sidebar/SidebarButton.tsx";
import { SidebarSection } from "@components/UI/Sidebar/SidebarSection.tsx";
import { useToast } from "@core/hooks/useToast.ts";
import { cn } from "@core/utils/cn.ts";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { DeviceConfig } from "@pages/Settings/DeviceConfig.tsx";
import { ModuleConfig } from "@pages/Settings/ModuleConfig.tsx";
import { useNavigate, useRouterState } from "@tanstack/react-router";
import {
  LayersIcon,
  RadioTowerIcon,
  RefreshCwIcon,
  RouterIcon,
  SaveIcon,
  SaveOff,
} from "lucide-react";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
...
```