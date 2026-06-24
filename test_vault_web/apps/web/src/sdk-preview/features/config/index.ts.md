# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/index.ts`
- **Extension:** `.ts`
- **Size:** 290 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts.md|apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/adapters/fromMeshDevice.ts.md|apps/web/src/sdk-preview/adapters/fromMeshDevice.ts]]
- [[apps/web/src/sdk-preview/index.ts.md|apps/web/src/sdk-preview/index.ts]]
- [[apps/web/src/sdk-preview/react/useConfigEditor.ts.md|apps/web/src/sdk-preview/react/useConfigEditor.ts]]

## Source Code Snippet
```ts
export { ConfigEditor } from "./domain/ConfigEditor.ts";
export type {
  ModuleConfig,
  ModuleConfigSection,
} from "./domain/ModuleConfig.ts";
export type { RadioConfig, RadioConfigSection } from "./domain/RadioConfig.ts";
export { ConfigMapper } from "./infrastructure/ConfigMapper.ts";
```