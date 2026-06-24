# Popover.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Popover.tsx`
- **Extension:** `.tsx`
- **Size:** 1029 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx.md|apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as PopoverPrimitive from "@radix-ui/react-popover";
import * as React from "react";

const Popover = PopoverPrimitive.Root;

const PopoverTrigger = PopoverPrimitive.Trigger;

const PopoverContent = React.forwardRef<
  React.ElementRef<typeof PopoverPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof PopoverPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <PopoverPrimitive.Portal>
    <PopoverPrimitive.Content
      ref={ref}
      align={align}
      sideOffset={sideOffset}
      className={cn(
        "z-50 w-72 rounded-md border border-slate-100 bg-white p-4 shadow-md outline-hidden animate-in data-[side=bottom]:slide-in-from-top-2 data-[side=top]:slide-in-from-bottom-2 dark:border-slate-800 dark:bg-slate-800",
        className,
...
```