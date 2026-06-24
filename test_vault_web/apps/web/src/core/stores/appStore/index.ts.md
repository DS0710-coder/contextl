# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/appStore/index.ts`
- **Extension:** `.ts`
- **Size:** 3246 bytes
- **Centrality Score:** 0.0029
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PersistOptions`
- `AppData`
- `AppState`

## Imports (Dependencies)
- [[apps/web/src/core/services/featureFlags.ts.md|apps/web/src/core/services/featureFlags.ts]]
- [[apps/web/src/core/stores/appStore/types.ts.md|apps/web/src/core/stores/appStore/types.ts]]
- [[apps/web/src/core/stores/utils/indexDB.ts.md|apps/web/src/core/stores/utils/indexDB.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/stores/appStore/appStore.test.ts.md|apps/web/src/core/stores/appStore/appStore.test.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Source Code Snippet
```ts
import { featureFlags } from "@core/services/featureFlags.ts";
import { createStorage } from "@core/stores/utils/indexDB.ts";
import { produce } from "immer";
import { create as createStore, type StateCreator } from "zustand";
import {
  type PersistOptions,
  persist,
  subscribeWithSelector,
} from "zustand/middleware";
import type { RasterSource } from "./types.ts";

const IDB_KEY_NAME = "meshtastic-app-store";
const CURRENT_STORE_VERSION = 0;

type AppData = {
  // Persisted data
  rasterSources: RasterSource[];
};

export interface AppState extends AppData {
...
```