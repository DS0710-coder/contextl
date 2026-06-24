# Link.tsx

## Architecture Metrics
- **Path:** `apps/web/src/__mocks__/components/UI/Link.tsx`
- **Extension:** `.tsx`
- **Size:** 322 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { vi } from "vitest";

vi.mock("@components/UI/Typography/Link.tsx", () => ({
  Link: ({
    children,
    href,
    className,
  }: {
    children: React.ReactNode;
    href: string;
    className?: string;
  }) => (
    <a data-testid="link" href={href} className={className}>
      {children}
    </a>
  ),
}));
```