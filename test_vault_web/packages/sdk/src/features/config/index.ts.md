# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/index.ts`
- **Extension:** `.ts`
- **Size:** 340 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/config/domain/ModuleConfig.ts.md|packages/sdk/src/features/config/domain/ModuleConfig.ts]]
- [[packages/sdk/src/features/config/domain/RadioConfig.ts.md|packages/sdk/src/features/config/domain/RadioConfig.ts]]
- [[packages/sdk/src/features/config/infrastructure/ConfigMapper.ts.md|packages/sdk/src/features/config/infrastructure/ConfigMapper.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { ConfigClient } from "./ConfigClient.ts";
export { ConfigEditor } from "./domain/ConfigEditor.ts";
export type { RadioConfig, RadioConfigSection } from "./domain/RadioConfig.ts";
export type {
  ModuleConfig,
  ModuleConfigSection,
} from "./domain/ModuleConfig.ts";
export { ConfigMapper } from "./infrastructure/ConfigMapper.ts";
```