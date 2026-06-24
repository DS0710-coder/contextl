# P.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/P.tsx`
- **Extension:** `.tsx`
- **Size:** 254 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";

export interface PProps {
  children: React.ReactNode;
  className?: string;
}

export const P = ({ children, className }: PProps) => (
  <p className={cn("leading-7 not-first:mt-6", className)}>{children}</p>
);
```