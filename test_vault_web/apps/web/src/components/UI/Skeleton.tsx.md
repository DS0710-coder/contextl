# Skeleton.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Skeleton.tsx`
- **Extension:** `.tsx`
- **Size:** 317 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Skeleton`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Messages/ChannelChat.tsx.md|apps/web/src/components/PageComponents/Messages/ChannelChat.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-md bg-slate-200 dark:bg-slate-700",
        className,
      )}
      {...props}
    />
  );
}

export { Skeleton };
```