# sort.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/sort.ts`
- **Extension:** `.ts`
- **Size:** 428 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `intlSort`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
export function intlSort<T extends PropertyKey>(
  arr: T[],
  locale: Intl.Locale,
  order: "asc" | "desc" = "asc",
): T[] {
  const collator = new Intl.Collator(locale, { sensitivity: "base" });

  return arr.sort((a, b) => {
    const stringA = String(a);
    const stringB = String(b);

    if (order === "asc") {
      return collator.compare(stringA, stringB);
    }
    return collator.compare(stringB, stringA);
  });
}
```