# indexDB.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/utils/indexDB.ts`
- **Extension:** `.ts`
- **Size:** 3762 bytes
- **Centrality Score:** 0.0031
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AnyRecord`
- `Envelope`
- `Handler`
- `isObject`
- `isEnvelope`
- `SerializedMap`
- `makeJson`
- `createStorage`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/stores/appStore/index.ts.md|apps/web/src/core/stores/appStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[apps/web/src/core/stores/utils/indexDB.test.ts.md|apps/web/src/core/stores/utils/indexDB.test.ts]]

## Source Code Snippet
```ts
import { del, get, set } from "idb-keyval";
import type {
  PersistStorage,
  StateStorage,
  StorageValue,
} from "zustand/middleware";

export const zustandIndexDBStorage: StateStorage = {
  getItem: async (name: string): Promise<string | null> => {
    return (await get(name)) || null;
  },
  setItem: async (name: string, value: string): Promise<void> => {
    await set(name, value);
  },
  removeItem: async (name: string): Promise<void> => {
    await del(name);
  },
};

type AnyRecord = Record<string, unknown>;
...
```