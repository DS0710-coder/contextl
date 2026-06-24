# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/core/index.ts`
- **Extension:** `.ts`
- **Size:** 298 bytes
- **Centrality Score:** 0.0024
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/client/MeshClientPort.ts.md|apps/web/src/sdk-preview/core/client/MeshClientPort.ts]]
- [[apps/web/src/sdk-preview/core/errors/MeshError.ts.md|apps/web/src/sdk-preview/core/errors/MeshError.ts]]
- [[apps/web/src/sdk-preview/core/signals/index.ts.md|apps/web/src/sdk-preview/core/signals/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/adapters/fromMeshDevice.ts.md|apps/web/src/sdk-preview/adapters/fromMeshDevice.ts]]
- [[apps/web/src/sdk-preview/features/config/__tests__/ConfigEditor.test.ts.md|apps/web/src/sdk-preview/features/config/__tests__/ConfigEditor.test.ts]]
- [[apps/web/src/sdk-preview/index.ts.md|apps/web/src/sdk-preview/index.ts]]
- [[apps/web/src/sdk-preview/react/useSignal.ts.md|apps/web/src/sdk-preview/react/useSignal.ts]]

## Source Code Snippet
```ts
export type {
  MeshClientEvents,
  MeshClientPort,
  Subscribable,
} from "./client/MeshClientPort.ts";
export {
  ConfigCommitError,
  MeshError,
  toMeshError,
} from "./errors/MeshError.ts";
export {
  createStore,
  type ReadonlySignal,
  SignalMap,
  toReadonly,
} from "./signals/index.ts";
```