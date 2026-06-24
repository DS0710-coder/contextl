# useConfigEditor.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useConfigEditor.ts`
- **Extension:** `.ts`
- **Size:** 591 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useConfigEditor`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ConfigEditor } from "@meshtastic/sdk";
import { useActiveClient } from "../adapters/useActiveClient.ts";

/**
 * Returns the active client's `ConfigEditor`, or `undefined` when no client
 * is active. The editor itself owns reactive signals — components bind to
 * `editor.radio.value`, `editor.dirtyRadioSections.value`, etc. via
 * `useSignal` (or the existing `useSignalValue`/`useSyncExternalStore`
 * helpers) to re-render on change.
 */
export function useConfigEditor(): ConfigEditor | undefined {
  const client = useActiveClient();
  return client?.config.editor;
}
```