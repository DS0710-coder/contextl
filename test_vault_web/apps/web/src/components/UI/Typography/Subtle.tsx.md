# Subtle.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/Subtle.tsx`
- **Extension:** `.tsx`
- **Size:** 295 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SubtleProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/ThemeSwitcher.tsx.md|apps/web/src/components/ThemeSwitcher.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";

export interface SubtleProps {
  className?: string;
  children: React.ReactNode;
}

export const Subtle = ({ className, children }: SubtleProps) => (
  <p className={cn("text-sm text-slate-500 dark:text-slate-400", className)}>
    {children}
  </p>
);
```