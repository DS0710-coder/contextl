# ConfigClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/ConfigClient.ts`
- **Extension:** `.ts`
- **Size:** 3323 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `ConfigClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/config/application/ConfigUseCases.ts.md|packages/sdk/src/features/config/application/ConfigUseCases.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/config/domain/ModuleConfig.ts.md|packages/sdk/src/features/config/domain/ModuleConfig.ts]]
- [[packages/sdk/src/features/config/domain/RadioConfig.ts.md|packages/sdk/src/features/config/domain/RadioConfig.ts]]
- [[packages/sdk/src/features/config/infrastructure/ConfigMapper.ts.md|packages/sdk/src/features/config/infrastructure/ConfigMapper.ts]]
- [[packages/sdk/src/features/config/state/configStore.ts.md|packages/sdk/src/features/config/state/configStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]

## Source Code Snippet
```ts
import * as Protobuf from "@meshtastic/protobufs";
import { computed } from "@preact/signals-core";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../core/signals/createStore.ts";
import {
  beginEditSettings,
  commitEditSettings,
  getConfig,
  getModuleConfig,
  setConfig,
  setModuleConfig,
} from "./application/ConfigUseCases.ts";
import { ConfigEditor } from "./domain/ConfigEditor.ts";
import type { ModuleConfig } from "./domain/ModuleConfig.ts";
import type { RadioConfig } from "./domain/RadioConfig.ts";
import { ConfigMapper } from "./infrastructure/ConfigMapper.ts";
...
```