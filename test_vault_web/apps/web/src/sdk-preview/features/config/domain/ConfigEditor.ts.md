# ConfigEditor.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts`
- **Extension:** `.ts`
- **Size:** 8841 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `ConfigEditor`
- `shallowEqual`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/client/MeshClientPort.ts.md|apps/web/src/sdk-preview/core/client/MeshClientPort.ts]]
- [[apps/web/src/sdk-preview/core/errors/MeshError.ts.md|apps/web/src/sdk-preview/core/errors/MeshError.ts]]
- [[apps/web/src/sdk-preview/core/signals/index.ts.md|apps/web/src/sdk-preview/core/signals/index.ts]]
- [[apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts.md|apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts.md|apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts]]
- [[apps/web/src/sdk-preview/features/config/infrastructure/configBuilders.ts.md|apps/web/src/sdk-preview/features/config/infrastructure/configBuilders.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/features/config/__tests__/ConfigEditor.test.ts.md|apps/web/src/sdk-preview/features/config/__tests__/ConfigEditor.test.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]

## Source Code Snippet
```ts
import { Types } from "@meshtastic/core";
import { signal } from "@preact/signals-core";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClientPort } from "../../../core/client/MeshClientPort.ts";
import type { MeshError } from "../../../core/errors/MeshError.ts";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../../core/signals/index.ts";
import {
  beginEditSettings,
  commitEditSettings,
  setConfig,
  setModuleConfig,
} from "../application/ConfigUseCases.ts";
import {
  buildModuleConfig,
  buildRadioConfig,
} from "../infrastructure/configBuilders.ts";
...
```