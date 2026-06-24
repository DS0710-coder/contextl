# Separator.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Separator.tsx`
- **Extension:** `.tsx`
- **Size:** 784 bytes
- **Centrality Score:** 0.0024
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/components/PageComponents/Messages/ChannelChat.tsx.md|apps/web/src/components/PageComponents/Messages/ChannelChat.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as SeparatorPrimitive from "@radix-ui/react-separator";
import * as React from "react";

const Separator = React.forwardRef<
  React.ComponentRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(
  (
    { className, orientation = "horizontal", decorative = true, ...props },
    ref,
  ) => (
    <SeparatorPrimitive.Root
      ref={ref}
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "bg-slate-200 dark:bg-slate-700",
        orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
        className,
...
```