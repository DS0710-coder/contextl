# utils.ts

## Architecture Metrics
- **Path:** `packages/ui/src/lib/utils.ts`
- **Extension:** `.ts`
- **Size:** 169 bytes
- **Centrality Score:** 0.0078
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `cn`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/ui/src/components/ui/badge.tsx.md|packages/ui/src/components/ui/badge.tsx]]
- [[packages/ui/src/components/ui/button.tsx.md|packages/ui/src/components/ui/button.tsx]]
- [[packages/ui/src/components/ui/dropdown-menu.tsx.md|packages/ui/src/components/ui/dropdown-menu.tsx]]
- [[packages/ui/src/components/ui/input.tsx.md|packages/ui/src/components/ui/input.tsx]]
- [[packages/ui/src/components/ui/separator.tsx.md|packages/ui/src/components/ui/separator.tsx]]
- [[packages/ui/src/components/ui/sheet.tsx.md|packages/ui/src/components/ui/sheet.tsx]]
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]
- [[packages/ui/src/components/ui/skeleton.tsx.md|packages/ui/src/components/ui/skeleton.tsx]]
- [[packages/ui/src/components/ui/tooltip.tsx.md|packages/ui/src/components/ui/tooltip.tsx]]
- [[packages/ui/src/lib/components/Sidebar/AppSidebar.tsx.md|packages/ui/src/lib/components/Sidebar/AppSidebar.tsx]]

## Source Code Snippet
```ts
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```