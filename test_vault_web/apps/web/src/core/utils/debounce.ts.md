# debounce.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/debounce.ts`
- **Extension:** `.ts`
- **Size:** 354 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Callback`
- `debounce`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/core/utils/debounce.test.ts.md|apps/web/src/core/utils/debounce.test.ts]]

## Source Code Snippet
```ts
type Callback<Args extends unknown[]> = (...args: Args) => void;

export function debounce<Args extends unknown[]>(
  callback: Callback<Args>,
  wait: number,
): Callback<Args> {
  let timeoutId: ReturnType<typeof setTimeout>;

  return (...args: Args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => callback(...args), wait);
  };
}
```