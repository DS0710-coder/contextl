# ToggleGroup.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/ToggleGroup.tsx`
- **Extension:** `.tsx`
- **Size:** 1957 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group";
import * as React from "react";

const toggleGroupItemClasses = [
  "flex flex-1 h-10 items-center justify-center first:rounded-l last:rounded-r ",
  "bg-slate-100",
  "dark:bg-slate-800",
  "data-[state=on]:bg-slate-600 data-[state=on]:text-white",
  "data-[state=on]:dark:bg-slate-950 data-[state=on]:text-white data-[state=on]:dark:text-slate-200",
  "data-[state=on]:hover:bg-slate-700 hover:bg-slate-700 hover:text-white hover:z-10 hover:shadow-[0_0_1px_2px] hover:outline-1 hover:outline-slate-700 hover:shadow-white/10",
  "data-[state=on]:dark:hover:bg-slate-700 dark:hover:bg-slate-700 dark:hover:text-slate-200 dark:hover:outline-slate-700 dark:hover:shadow-black/20",
  "disabled:text-slate-300 disabled:hover:bg-slate-100 disabled:hover:outline-none hover:shadow-none disabled:dark:text-slate-600 disabled:dark:hover:bg-slate-800 disabled:dark:hover:outline-none disabled:shadow-none",
];

const ToggleGroup = React.forwardRef<
  React.ComponentRef<typeof ToggleGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Root>
>(({ className, ...props }, ref) => (
  <ToggleGroupPrimitive.Root
...
```