# bindStoreToDevice.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/utils/bindStoreToDevice.ts`
- **Extension:** `.ts`
- **Size:** 3214 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GenericEqualityFn`
- `DebounceOpts`
- `StoreWithSelector`
- `bindStoreToDevice`
- `useBound`
- `useBound`
- `useBound`
- `Selected`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useDeviceContext.ts.md|apps/web/src/core/hooks/useDeviceContext.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { useDeviceContext } from "@core/hooks/useDeviceContext";
import { useCallback, useMemo, useRef, useSyncExternalStore } from "react";
import type { StoreApi, UseBoundStore } from "zustand";
import { shallow } from "zustand/shallow";

type GenericEqualityFn<T> = (a: T, b: T) => boolean;

type DebounceOpts<T> = {
  debounce?: number; // 0/undefined = no debounce
  equality?: GenericEqualityFn<T>; // default: shallow
  fireImmediately?: boolean; // default: true
};

type StoreWithSelector<S> = UseBoundStore<StoreApi<S>> & {
  getState(): S;
  subscribe: <U>(
    selector: (state: S) => U,
    listener: (next: U, prev: U) => void,
    options?: { equalityFn?: GenericEqualityFn<U>; fireImmediately?: boolean },
  ) => () => void;
...
```