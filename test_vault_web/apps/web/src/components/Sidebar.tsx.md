# Sidebar.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Sidebar.tsx`
- **Extension:** `.tsx`
- **Size:** 7209 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Page`
- `LucideIcon`
- `SidebarProps`
- `NavLink`

## Imports (Dependencies)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarButton.tsx.md|apps/web/src/components/UI/Sidebar/SidebarButton.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarSection.tsx.md|apps/web/src/components/UI/Sidebar/SidebarSection.tsx]]
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/deviceStore/selectors.ts.md|apps/web/src/core/stores/deviceStore/selectors.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { useFirstSavedConnection } from "@app/core/stores/deviceStore/selectors.ts";
import { SidebarButton } from "@components/UI/Sidebar/SidebarButton.tsx";
import { SidebarSection } from "@components/UI/Sidebar/SidebarSection.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import { Subtle } from "@components/UI/Typography/Subtle.tsx";
import {
  useMyNodeAsProto,
  useNodesAsProto,
} from "@core/hooks/useNodesAsProto.ts";
import {
  type Page,
  useActiveConnection,
  useAppStore,
  useDefaultConnection,
  useDevice,
  useSidebar,
} from "@core/stores";
import { cn } from "@core/utils/cn.ts";
import { useTotalUnread } from "@meshtastic/sdk-react";
import { useLocation, useNavigate } from "@tanstack/react-router";
...
```