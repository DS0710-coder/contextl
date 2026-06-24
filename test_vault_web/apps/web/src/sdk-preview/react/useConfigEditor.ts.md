# useConfigEditor.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/react/useConfigEditor.ts`
- **Extension:** `.ts`
- **Size:** 763 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useConfigEditor`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/sdk-preview/adapters/fromMeshDevice.ts.md|apps/web/src/sdk-preview/adapters/fromMeshDevice.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/index.ts.md|apps/web/src/sdk-preview/index.ts]]

## Source Code Snippet
```ts
import { useDevice } from "@core/stores";
import { getConfigEditor } from "../adapters/fromMeshDevice.ts";
import type { ConfigEditor } from "../features/config/index.ts";

/**
 * Returns the active connection's `ConfigEditor`, or `undefined` when nothing is
 * connected. The editor owns reactive signals — components bind to
 * `editor.radio`, `editor.dirtyModuleSections`, `editor.isDirty`, etc. via
 * `useSignal` to re-render on change. Mirrors `useConfigEditor` from
 * `@meshtastic/sdk-react` (PR #1050), sourced here from the legacy device
 * connection rather than a `MeshRegistry`.
 */
export function useConfigEditor(): ConfigEditor | undefined {
  const { connection } = useDevice();
  return connection ? getConfigEditor(connection) : undefined;
}
```