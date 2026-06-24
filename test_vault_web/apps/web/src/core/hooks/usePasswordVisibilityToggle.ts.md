# usePasswordVisibilityToggle.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/usePasswordVisibilityToggle.ts`
- **Extension:** `.ts`
- **Size:** 630 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UsePasswordVisibilityToggleProps`
- `usePasswordVisibilityToggle`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Form/FormPasswordGenerator.tsx.md|apps/web/src/components/Form/FormPasswordGenerator.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/core/hooks/usePasswordVisibilityToggle.test.ts.md|apps/web/src/core/hooks/usePasswordVisibilityToggle.test.ts]]

## Source Code Snippet
```ts
import { useCallback, useState } from "react";

interface UsePasswordVisibilityToggleProps {
  initialVisible?: boolean;
}
/**
 * Manages the state for toggling password visibility.
 *
 * @param {boolean} [options.initialVisible=false]
 * @returns {{isVisible: boolean, toggleVisibility: () => void}}
 */
export function usePasswordVisibilityToggle({
  initialVisible = false,
}: UsePasswordVisibilityToggleProps = {}) {
  const [isVisible, setIsVisible] = useState<boolean>(initialVisible);

  const toggleVisibility = useCallback(() => {
    setIsVisible((prev) => !prev);
  }, []);

...
```