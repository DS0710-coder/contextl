# Toast.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Toast.tsx`
- **Extension:** `.tsx`
- **Size:** 4959 bytes
- **Centrality Score:** 0.0051
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ToastProps`
- `ToastActionElement`
- `ToastActionElement`
- `ToastProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Toaster.tsx.md|apps/web/src/components/Toaster.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]

## Source Code Snippet
```tsx
import * as ToastPrimitives from "@radix-ui/react-toast";
import { cva, type VariantProps } from "class-variance-authority";
import { X } from "lucide-react";
import * as React from "react";

import { cn } from "../../core/utils/cn.ts";

const ToastProvider = ToastPrimitives.Provider;

const ToastViewport = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Viewport>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Viewport>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Viewport
    ref={ref}
    className={cn(
      "fixed top-0 z-100 flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-24 sm:right-6 sm:top-auto sm:flex-col md:max-w-[420px]",
      className,
    )}
    {...props}
...
```