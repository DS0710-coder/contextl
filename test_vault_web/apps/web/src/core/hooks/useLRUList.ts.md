# useLRUList.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useLRUList.ts`
- **Extension:** `.ts`
- **Size:** 6421 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PersistedPayload`
- `UseLRUListOptions`
- `UseLRUListReturn`
- `useLRUList`
- `trimToCapacity`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { useCallback, useEffect, useMemo, useRef, useState } from "react";

/**
 * A minimal serializable wrapper so we can store metadata alongside items.
 */
type PersistedPayload<J = unknown> = {
  v: 1; // schema version
  capacity: number; // last used capacity (for info/migrations)
  items: J[]; // serialized items (MRU -> LRU)
};

export type UseLRUListOptions<T, J = unknown> = {
  /** localStorage key */
  key: string;
  /** max number of items to keep (>=1) */
  capacity: number;
  /** optional initial items used when storage is empty/invalid */
  initial?: T[];
  /** equality to de-duplicate items; default: Object.is */
  eq?: (a: T, b: T) => boolean;
...
```