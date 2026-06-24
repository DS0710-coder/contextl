# evictOldestEntries.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/utils/evictOldestEntries.ts`
- **Extension:** `.ts`
- **Size:** 739 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `evictOldestEntries`
- `evictOldestEntries`
- `evictOldestEntries`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]

## Source Code Snippet
```ts
export function evictOldestEntries<T>(arr: T[], maxSize: number): void;
export function evictOldestEntries<K, V>(map: Map<K, V>, maxSize: number): void;

export function evictOldestEntries<T, K, V>(
  collection: T[] | Map<K, V>,
  maxSize: number,
): void {
  if (Array.isArray(collection)) {
    // Trim array from the front (assuming oldest entries are at the start)
    while (collection.length > maxSize) {
      collection.shift();
    }
  } else if (collection instanceof Map) {
    // Trim map by insertion order
    while (collection.size > maxSize) {
      const firstKey = collection.keys().next().value;
      if (firstKey !== undefined) {
        collection.delete(firstKey);
      } else {
        break;
...
```