# useSignalValue.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useSignalValue.ts`
- **Extension:** `.ts`
- **Size:** 676 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useSignalValue`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/hooks/useNode.ts.md|packages/sdk-react/src/hooks/useNode.ts]]
- [[packages/sdk-react/src/hooks/usePosition.ts.md|packages/sdk-react/src/hooks/usePosition.ts]]
- [[packages/sdk-react/src/hooks/useTraceroute.ts.md|packages/sdk-react/src/hooks/useTraceroute.ts]]

## Source Code Snippet
```ts
import type { ReadonlySignal } from "@meshtastic/sdk";
import { useCallback, useSyncExternalStore } from "react";

/**
 * Like `useSignal` but projects the signal value through a selector before
 * returning. The selector should be stable; memoize it with `useCallback` in
 * the caller when it closes over changing values.
 */
export function useSignalValue<T, U>(
  sig: ReadonlySignal<T>,
  select: (value: T) => U,
): U {
  const getSnapshot = useCallback(() => select(sig.value), [sig, select]);
  const getServerSnapshot = useCallback(
    () => select(sig.peek()),
    [sig, select],
  );
  return useSyncExternalStore(sig.subscribe, getSnapshot, getServerSnapshot);
}
```