# tooltip.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/ui/tooltip.tsx`
- **Extension:** `.tsx`
- **Size:** 1892 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TooltipProvider`
- `Tooltip`
- `TooltipTrigger`
- `TooltipContent`

## Imports (Dependencies)
- [[packages/ui/src/lib/utils.ts.md|packages/ui/src/lib/utils.ts]]

## Imported By (Dependents)
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]

## Source Code Snippet
```tsx
import * as TooltipPrimitive from "@radix-ui/react-tooltip";
import type * as React from "react";

import { cn } from "@/lib/utils";

function TooltipProvider({
  delayDuration = 0,
  ...props
}: React.ComponentProps<typeof TooltipPrimitive.Provider>) {
  return (
    <TooltipPrimitive.Provider
      data-slot="tooltip-provider"
      delayDuration={delayDuration}
      {...props}
    />
  );
}

function Tooltip({
  ...props
...
```