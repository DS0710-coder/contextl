# Button.tsx

## Architecture Metrics
- **Path:** `apps/web/src/__mocks__/components/UI/Button.tsx`
- **Extension:** `.tsx`
- **Size:** 460 bytes
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

vi.mock("@components/UI/Button.tsx", () => ({
  Button: ({
    children,
    name,
    disabled,
    onClick,
  }: {
    children: React.ReactNode;
    variant: string;
    name: string;
    disabled?: boolean;
    onClick: () => void;
  }) => (
    <button
      type="button"
      name={name}
      data-testid={`button-${name}`}
      disabled={disabled}
...
```