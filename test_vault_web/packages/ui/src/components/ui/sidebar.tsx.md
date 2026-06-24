# sidebar.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/ui/sidebar.tsx`
- **Extension:** `.tsx`
- **Size:** 21841 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SidebarContextProps`
- `useSidebar`
- `SidebarProvider`
- `Sidebar`
- `SidebarTrigger`
- `SidebarRail`
- `SidebarInset`
- `SidebarInput`
- `SidebarHeader`
- `SidebarFooter`
- `SidebarSeparator`
- `SidebarContent`
- `SidebarGroup`
- `SidebarGroupLabel`
- `SidebarGroupAction`
- `SidebarGroupContent`
- `SidebarMenu`
- `SidebarMenuItem`
- `SidebarMenuButton`
- `SidebarMenuAction`
- `SidebarMenuBadge`
- `SidebarMenuSkeleton`
- `SidebarMenuSub`
- `SidebarMenuSubItem`
- `SidebarMenuSubButton`

## Imports (Dependencies)
- [[packages/ui/src/components/ui/button.tsx.md|packages/ui/src/components/ui/button.tsx]]
- [[packages/ui/src/components/ui/input.tsx.md|packages/ui/src/components/ui/input.tsx]]
- [[packages/ui/src/components/ui/separator.tsx.md|packages/ui/src/components/ui/separator.tsx]]
- [[packages/ui/src/components/ui/sheet.tsx.md|packages/ui/src/components/ui/sheet.tsx]]
- [[packages/ui/src/components/ui/skeleton.tsx.md|packages/ui/src/components/ui/skeleton.tsx]]
- [[packages/ui/src/components/ui/tooltip.tsx.md|packages/ui/src/components/ui/tooltip.tsx]]
- [[packages/ui/src/hooks/use-mobile.ts.md|packages/ui/src/hooks/use-mobile.ts]]
- [[packages/ui/src/lib/utils.ts.md|packages/ui/src/lib/utils.ts]]

## Imported By (Dependents)
- [[packages/ui/src/index.ts.md|packages/ui/src/index.ts]]
- [[packages/ui/src/lib/components/Sidebar/AppSidebar.tsx.md|packages/ui/src/lib/components/Sidebar/AppSidebar.tsx]]

## Source Code Snippet
```tsx
"use client";

import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { PanelLeftIcon } from "lucide-react";
import * as React from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import { Skeleton } from "@/components/ui/skeleton";
import {
  Tooltip,
  TooltipContent,
...
```