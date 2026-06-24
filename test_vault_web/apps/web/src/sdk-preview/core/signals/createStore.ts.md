# createStore.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/core/signals/createStore.ts`
- **Extension:** `.ts`
- **Size:** 2724 bytes
- **Centrality Score:** 0.0021
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `Signal`
- `ReadonlySignal`
- `createStore`
- `toReadonly`
- `SignalMap`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/core/signals/index.ts.md|apps/web/src/sdk-preview/core/signals/index.ts]]

## Source Code Snippet
```ts
import {
  type ReadonlySignal as PreactReadonlySignal,
  type Signal,
  signal,
} from "@preact/signals-core";

/**
 * Reactive read-only view of a signal.
 *
 * Compatible with React's `useSyncExternalStore` contract: consumers subscribe
 * for change notifications and call `value` / `peek()` to read.
 *
 * Mirrors `@meshtastic/sdk`'s core signals primitive from PR #1050. The point
 * of this preview slice is to show the *shape* of the SDK direction inside the
 * current app without pulling in the whole SDK + sqlocal stack.
 */
export interface ReadonlySignal<T> {
  readonly value: T;
  peek(): T;
  subscribe(listener: (value: T) => void): () => void;
...
```