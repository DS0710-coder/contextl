# AppSidebar.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/lib/components/Sidebar/AppSidebar.tsx`
- **Extension:** `.tsx`
- **Size:** 7131 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AppSidebarProps`
- `NavLink`
- `SidebarSectionProps`

## Imports (Dependencies)
- [[packages/ui/src/components/ui/badge.tsx.md|packages/ui/src/components/ui/badge.tsx]]
- [[packages/ui/src/components/ui/collapsible.tsx.md|packages/ui/src/components/ui/collapsible.tsx]]
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]
- [[packages/ui/src/lib/utils.ts.md|packages/ui/src/lib/utils.ts]]

## Imported By (Dependents)
- [[packages/ui/src/index.ts.md|packages/ui/src/index.ts]]
- [[packages/ui/src/lib/components/index.ts.md|packages/ui/src/lib/components/index.ts]]

## Source Code Snippet
```tsx
import type { LucideIcon } from "lucide-react";
import { ChevronRight } from "lucide-react";
import type * as React from "react";
import { Badge } from "@/components/ui/badge";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
...
```