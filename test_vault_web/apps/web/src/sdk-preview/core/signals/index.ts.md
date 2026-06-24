# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/core/signals/index.ts`
- **Extension:** `.ts`
- **Size:** 101 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/signals/createStore.ts.md|apps/web/src/sdk-preview/core/signals/createStore.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
export {
  createStore,
  type ReadonlySignal,
  SignalMap,
  toReadonly,
} from "./createStore.ts";
```