# Mono.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Mono.tsx`
- **Extension:** `.tsx`
- **Size:** 386 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MonoProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/generic/Table/index.test.tsx.md|apps/web/src/components/generic/Table/index.test.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";

interface MonoProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  className?: string;
}
export const Mono = ({ children, className, ...rest }: MonoProps) => {
  return (
    <span
      className={cn("font-mono text-sm text-text-secondary", className)}
      {...rest}
    >
      {children}
    </span>
  );
};
```