# Card.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Card.tsx`
- **Extension:** `.tsx`
- **Size:** 2026 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as React from "react";

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-lg border border-slate-200 bg-white text-slate-900 shadow-sm dark:border-slate-700 dark:bg-slate-800 dark:text-slate-100",
      className,
    )}
    {...props}
  />
));
Card.displayName = "Card";

const CardHeader = React.forwardRef<
  HTMLDivElement,
...
```