# useSignal.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useSignal.ts`
- **Extension:** `.ts`
- **Size:** 490 bytes
- **Centrality Score:** 0.0071
- **In-Degree (Imported By):** 16
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useSignal`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/hooks/useChannels.ts.md|packages/sdk-react/src/hooks/useChannels.ts]]
- [[packages/sdk-react/src/hooks/useChat.ts.md|packages/sdk-react/src/hooks/useChat.ts]]
- [[packages/sdk-react/src/hooks/useConfig.ts.md|packages/sdk-react/src/hooks/useConfig.ts]]
- [[packages/sdk-react/src/hooks/useConnection.ts.md|packages/sdk-react/src/hooks/useConnection.ts]]
- [[packages/sdk-react/src/hooks/useConnectionProgress.ts.md|packages/sdk-react/src/hooks/useConnectionProgress.ts]]
- [[packages/sdk-react/src/hooks/useDirectChat.ts.md|packages/sdk-react/src/hooks/useDirectChat.ts]]
- [[packages/sdk-react/src/hooks/useDraft.ts.md|packages/sdk-react/src/hooks/useDraft.ts]]
- [[packages/sdk-react/src/hooks/useFileTransfer.ts.md|packages/sdk-react/src/hooks/useFileTransfer.ts]]
- [[packages/sdk-react/src/hooks/useMeshDevice.ts.md|packages/sdk-react/src/hooks/useMeshDevice.ts]]
- [[packages/sdk-react/src/hooks/useNodeError.ts.md|packages/sdk-react/src/hooks/useNodeError.ts]]
- [[packages/sdk-react/src/hooks/useNodes.ts.md|packages/sdk-react/src/hooks/useNodes.ts]]
- [[packages/sdk-react/src/hooks/useTelemetry.ts.md|packages/sdk-react/src/hooks/useTelemetry.ts]]
- [[packages/sdk-react/src/hooks/useUnread.ts.md|packages/sdk-react/src/hooks/useUnread.ts]]

## Source Code Snippet
```ts
import type { ReadonlySignal } from "@meshtastic/sdk";
import { useSyncExternalStore } from "react";

/**
 * Subscribes a component to a SDK ReadonlySignal and returns the current value.
 *
 * Uses useSyncExternalStore so concurrent-mode renders see a consistent
 * snapshot. The signal's `.subscribe` is called once per mount.
 */
export function useSignal<T>(sig: ReadonlySignal<T>): T {
  return useSyncExternalStore(
    sig.subscribe,
    () => sig.value,
    () => sig.peek(),
  );
}
```