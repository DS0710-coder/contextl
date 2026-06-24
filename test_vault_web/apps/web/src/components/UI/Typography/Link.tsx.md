# Link.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/Link.tsx`
- **Extension:** `.tsx`
- **Size:** 691 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LinkProps`
- `LinkProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import {
  Link as RouterLink,
  type LinkProps as RouterLinkProps,
} from "@tanstack/react-router";

export interface LinkProps extends RouterLinkProps {
  href: string;
  children?:
    | React.ReactNode
    | ((state: {
        isActive: boolean;
        isTransitioning: boolean;
      }) => React.ReactNode);
  className?: string;
}

export const Link = ({ href, children, className }: LinkProps) => (
  <RouterLink
    to={href}
...
```