# Command.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Command.tsx`
- **Extension:** `.tsx`
- **Size:** 5225 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]

## Source Code Snippet
```tsx
import { Dialog, DialogContent, DialogTitle } from "@components/UI/Dialog.tsx";
import { cn } from "@core/utils/cn.ts";
import type { DialogProps } from "@radix-ui/react-dialog";
import { VisuallyHidden } from "@radix-ui/react-visually-hidden";
import { Command as CommandPrimitive } from "cmdk";
import { Search } from "lucide-react";
import * as React from "react";

const Command = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive>
>(({ className, ...props }, ref) => (
  <CommandPrimitive
    ref={ref}
    className={cn(
      "flex h-full w-full flex-col overflow-hidden rounded-lg bg-white dark:bg-slate-800",
      className,
    )}
    {...props}
  />
...
```