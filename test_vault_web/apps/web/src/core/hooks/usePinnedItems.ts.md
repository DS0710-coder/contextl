# usePinnedItems.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/usePinnedItems.ts`
- **Extension:** `.ts`
- **Size:** 573 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `usePinnedItems`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useLocalStorage.ts.md|apps/web/src/core/hooks/useLocalStorage.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]

## Source Code Snippet
```ts
import useLocalStorage from "@core/hooks/useLocalStorage.ts";
import { useCallback } from "react";

export function usePinnedItems({ storageName }: { storageName: string }) {
  const [pinnedItems, setPinnedItems] = useLocalStorage<string[]>(
    storageName,
    [],
  );

  const togglePinnedItem = useCallback(
    (label: string) => {
      setPinnedItems((prev) =>
        prev.includes(label)
          ? prev.filter((g) => g !== label)
          : [...prev, label],
      );
    },
    [setPinnedItems],
  );

...
```