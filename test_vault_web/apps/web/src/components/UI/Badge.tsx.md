# Badge.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Badge.tsx`
- **Extension:** `.tsx`
- **Size:** 1314 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BadgeProps`
- `Badge`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Badge/SupportedBadge.tsx.md|apps/web/src/components/Badge/SupportedBadge.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-slate-900 text-white hover:bg-slate-900/80 dark:bg-slate-50 dark:text-slate-900 dark:hover:bg-slate-50/80",
        secondary:
          "border-transparent bg-slate-100 text-slate-900 hover:bg-slate-100/80 dark:bg-slate-800 dark:text-slate-100 dark:hover:bg-slate-800/80",
        destructive:
          "border-transparent bg-red-500 text-white hover:bg-red-500/80 dark:bg-red-900 dark:text-red-50 dark:hover:bg-red-900/80",
        outline: "text-slate-900 dark:text-slate-100",
      },
    },
    defaultVariants: {
      variant: "default",
...
```