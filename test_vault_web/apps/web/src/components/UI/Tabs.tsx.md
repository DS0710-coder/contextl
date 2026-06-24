# Tabs.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Tabs.tsx`
- **Extension:** `.tsx`
- **Size:** 1743 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as TabsPrimitive from "@radix-ui/react-tabs";
import * as React from "react";

const Tabs = TabsPrimitive.Root;

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex flex-wrap items-center rounded-md  p-1 mt-2 bg-slate-200 dark:bg-slate-100",
      className,
    )}
    {...props}
  />
));
TabsList.displayName = TabsPrimitive.List.displayName;
...
```