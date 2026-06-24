# sheet.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/ui/sheet.tsx`
- **Extension:** `.tsx`
- **Size:** 4114 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Sheet`
- `SheetTrigger`
- `SheetClose`
- `SheetPortal`
- `SheetOverlay`
- `SheetContent`
- `SheetHeader`
- `SheetFooter`
- `SheetTitle`
- `SheetDescription`

## Imports (Dependencies)
- [[packages/ui/src/lib/utils.ts.md|packages/ui/src/lib/utils.ts]]

## Imported By (Dependents)
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]

## Source Code Snippet
```tsx
"use client";

import * as SheetPrimitive from "@radix-ui/react-dialog";
import { XIcon } from "lucide-react";
import type * as React from "react";

import { cn } from "@/lib/utils";

function Sheet({ ...props }: React.ComponentProps<typeof SheetPrimitive.Root>) {
  return <SheetPrimitive.Root data-slot="sheet" {...props} />;
}

function SheetTrigger({
  ...props
}: React.ComponentProps<typeof SheetPrimitive.Trigger>) {
  return <SheetPrimitive.Trigger data-slot="sheet-trigger" {...props} />;
}

function SheetClose({
  ...props
...
```