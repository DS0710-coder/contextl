# useSignal.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/react/useSignal.ts`
- **Extension:** `.ts`
- **Size:** 497 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useSignal`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/index.ts.md|apps/web/src/sdk-preview/index.ts]]

## Source Code Snippet
```ts
import { useSyncExternalStore } from "react";
import type { ReadonlySignal } from "../core/index.ts";

/**
 * Subscribes a component to a `ReadonlySignal` and returns its current value.
 *
 * Uses `useSyncExternalStore` so concurrent-mode renders see a consistent
 * snapshot. Mirrors `@meshtastic/sdk-react`'s `useSignal` (PR #1050).
 */
export function useSignal<T>(sig: ReadonlySignal<T>): T {
  return useSyncExternalStore(
    sig.subscribe,
    () => sig.value,
    () => sig.peek(),
  );
}
```