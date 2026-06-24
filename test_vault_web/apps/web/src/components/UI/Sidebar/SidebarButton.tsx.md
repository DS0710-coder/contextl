# SidebarButton.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Sidebar/SidebarButton.tsx`
- **Extension:** `.tsx`
- **Size:** 2144 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SidebarButtonProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { useSidebar } from "@core/stores";
import { cn } from "@core/utils/cn.ts";
import type { LucideIcon } from "lucide-react";
import type React from "react";

export interface SidebarButtonProps {
  label: string;
  count?: number;
  active?: boolean;
  Icon?: LucideIcon;
  children?: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  preventCollapse?: boolean;
  isDirty?: boolean;
}

export const SidebarButton = ({
  label,
...
```