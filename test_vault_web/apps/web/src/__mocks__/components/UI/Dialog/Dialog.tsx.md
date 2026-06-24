# Dialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/__mocks__/components/UI/Dialog/Dialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1135 bytes
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
import type React from "react";

export const Dialog = ({
  children,
  open,
}: {
  children: React.ReactNode;
  open: boolean;
  onOpenChange?: (open: boolean) => void;
}) => (open ? <div data-testid="dialog">{children}</div> : null);

export const DialogContent = ({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) => (
  <div data-testid="dialog-content" className={className}>
    {children}
...
```