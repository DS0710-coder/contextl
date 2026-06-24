# useToggleVisiblility.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useToggleVisiblility.ts`
- **Extension:** `.ts`
- **Size:** 795 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useToggleVisibility`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/ThemeSwitcher.tsx.md|apps/web/src/components/ThemeSwitcher.tsx]]

## Source Code Snippet
```ts
import { useCallback, useEffect, useRef, useState } from "react";

export function useToggleVisibility({ timeout }: { timeout?: number } = {}) {
  const [isVisible, setIsVisible] = useState(false);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const show = useCallback(() => {
    setIsVisible(true);

    if (timeout) {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }

      timeoutRef.current = setTimeout(() => {
        setIsVisible(false);
        timeoutRef.current = null;
      }, timeout);
    }
  }, [timeout]);
...
```