# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/index.ts`
- **Extension:** `.ts`
- **Size:** 489 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/adapters/fromMeshDevice.ts.md|apps/web/src/sdk-preview/adapters/fromMeshDevice.ts]]
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]
- [[apps/web/src/sdk-preview/react/useConfigEditor.ts.md|apps/web/src/sdk-preview/react/useConfigEditor.ts]]
- [[apps/web/src/sdk-preview/react/useSignal.ts.md|apps/web/src/sdk-preview/react/useSignal.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
// Public surface of the SDK-direction preview slice. See ./README.md.
export * from "./core/index.ts";
export { ConfigEditor } from "./features/config/index.ts";
export type {
  ModuleConfig,
  ModuleConfigSection,
  RadioConfig,
  RadioConfigSection,
} from "./features/config/index.ts";
export {
  getConfigEditor,
  meshDeviceToPort,
} from "./adapters/fromMeshDevice.ts";
export { useConfigEditor } from "./react/useConfigEditor.ts";
export { useSignal } from "./react/useSignal.ts";
```