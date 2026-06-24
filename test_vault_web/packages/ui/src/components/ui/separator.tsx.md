# separator.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/ui/separator.tsx`
- **Extension:** `.tsx`
- **Size:** 696 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Separator`

## Imports (Dependencies)
- [[packages/ui/src/lib/utils.ts.md|packages/ui/src/lib/utils.ts]]

## Imported By (Dependents)
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]

## Source Code Snippet
```tsx
import * as SeparatorPrimitive from "@radix-ui/react-separator";
import type * as React from "react";

import { cn } from "@/lib/utils";

function Separator({
  className,
  orientation = "horizontal",
  decorative = true,
  ...props
}: React.ComponentProps<typeof SeparatorPrimitive.Root>) {
  return (
    <SeparatorPrimitive.Root
      data-slot="separator"
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px",
        className,
      )}
...
```