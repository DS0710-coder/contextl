# configStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/state/configStore.ts`
- **Extension:** `.ts`
- **Size:** 399 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createConfigStore`
- `ConfigStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/config/domain/ModuleConfig.ts.md|packages/sdk/src/features/config/domain/ModuleConfig.ts]]
- [[packages/sdk/src/features/config/domain/RadioConfig.ts.md|packages/sdk/src/features/config/domain/RadioConfig.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]

## Source Code Snippet
```ts
import { createStore } from "../../../core/signals/createStore.ts";
import type { ModuleConfig } from "../domain/ModuleConfig.ts";
import type { RadioConfig } from "../domain/RadioConfig.ts";

export function createConfigStore() {
  return {
    radio: createStore<RadioConfig>({}),
    modules: createStore<ModuleConfig>({}),
  };
}

export type ConfigStore = ReturnType<typeof createConfigStore>;
```