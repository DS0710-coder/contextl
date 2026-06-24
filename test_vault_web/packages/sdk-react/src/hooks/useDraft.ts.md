# useDraft.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useDraft.ts`
- **Extension:** `.ts`
- **Size:** 1040 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseDraftResult`
- `useDraft`
- `keyOf`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ConversationKey } from "@meshtastic/sdk";
import { useCallback, useMemo } from "react";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseDraftResult {
  text: string;
  setText(value: string): void;
  clear(): void;
}

/**
 * Per-conversation draft text bound to the SDK chat slice. Re-renders on
 * every change. Auto-clears when send() succeeds.
 */
export function useDraft(conv: ConversationKey): UseDraftResult {
  const client = useClient();
  const sig = useMemo(
    () => client.chat.drafts.get(conv),
    [client, conv.kind, keyOf(conv)],
...
```