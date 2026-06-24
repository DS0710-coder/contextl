# Toaster.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Toaster.tsx`
- **Extension:** `.tsx`
- **Size:** 813 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Toaster`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Toast.tsx.md|apps/web/src/components/UI/Toast.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]

## Source Code Snippet
```tsx
import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "@components/UI/Toast.tsx";
import { useToast } from "@core/hooks/useToast.ts";

export function Toaster() {
  const { toasts } = useToast();

  return (
    <ToastProvider>
      {toasts.map(({ id, title, description, action, duration, ...props }) => (
        <Toast
          key={id}
          {...props}
          duration={duration}
...
```