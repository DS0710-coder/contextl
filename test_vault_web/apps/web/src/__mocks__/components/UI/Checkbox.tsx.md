# Checkbox.tsx

## Architecture Metrics
- **Path:** `apps/web/src/__mocks__/components/UI/Checkbox.tsx`
- **Extension:** `.tsx`
- **Size:** 352 bytes
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

vi.mock("@components/UI/Checkbox.tsx", () => ({
  Checkbox: ({
    id,
    checked,
    onChange,
  }: {
    id: string;
    checked: boolean;
    onChange: () => void;
  }) => (
    <input
      data-testid="checkbox"
      type="checkbox"
      id={id}
      checked={checked}
      onChange={onChange}
    />
  ),
...
```