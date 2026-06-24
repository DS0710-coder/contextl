# Accordion.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Accordion.tsx`
- **Extension:** `.tsx`
- **Size:** 1361 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as AccordionPrimitive from "@radix-ui/react-accordion";
import { ChevronDownIcon } from "lucide-react";
import { type ComponentRef, forwardRef } from "react";

export const Accordion = AccordionPrimitive.Root;

export const AccordionHeader = AccordionPrimitive.Header;

export const AccordionItem = AccordionPrimitive.Item;

export const AccordionTrigger = forwardRef<
  ComponentRef<typeof AccordionPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex justify-between items-center w-full p-4 border-b border-slate-200 dark:border-slate-800 group",
      className,
...
```