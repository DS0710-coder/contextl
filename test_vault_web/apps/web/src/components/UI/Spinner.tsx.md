# Spinner.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Spinner.tsx`
- **Extension:** `.tsx`
- **Size:** 2242 bytes
- **Centrality Score:** 0.0013
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SpinnerProps`
- `Spinner`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]

## Source Code Snippet
```tsx
import { cn } from "../../core/utils/cn.ts";

interface SpinnerProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: "sm" | "md" | "lg";
}

const sizeClasses = {
  sm: "h-4 w-4",
  md: "h-8 w-8",
  lg: "h-12 w-12",
};

export function Spinner({ className, size = "md", ...props }: SpinnerProps) {
  return (
    <div
      className={cn(
        "flex items-center justify-center fade-in-50 fade-out-50",
        className,
      )}
      {...props}
...
```