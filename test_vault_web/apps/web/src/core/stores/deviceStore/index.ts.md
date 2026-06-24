# index.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/deviceStore/index.ts`
- **Extension:** `.ts`
- **Size:** 25585 bytes
- **Centrality Score:** 0.0044
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PersistOptions`
- `DeviceData`
- `ConnectionPhase`
- `Device`
- `deviceState`
- `PrivateDeviceState`
- `DevicePersisted`
- `deviceFactory`

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/stores/utils/evictOldestEntries.ts.md|apps/web/src/core/stores/utils/evictOldestEntries.ts]]
- [[apps/web/src/core/stores/utils/indexDB.ts.md|apps/web/src/core/stores/utils/indexDB.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/stores/deviceStore/deviceStore.mock.ts.md|apps/web/src/core/stores/deviceStore/deviceStore.mock.ts]]
- [[apps/web/src/core/stores/deviceStore/deviceStore.test.ts.md|apps/web/src/core/stores/deviceStore/deviceStore.test.ts]]
- [[apps/web/src/core/stores/deviceStore/selectors.ts.md|apps/web/src/core/stores/deviceStore/selectors.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import { evictOldestEntries } from "@core/stores/utils/evictOldestEntries.ts";
import { createStorage } from "@core/stores/utils/indexDB.ts";
import { type MeshDevice, Protobuf, Types } from "@meshtastic/sdk";
import { type Draft, produce } from "immer";
import { create as createStore, type StateCreator } from "zustand";
import {
  type PersistOptions,
  persist,
  subscribeWithSelector,
} from "zustand/middleware";
import type {
  Connection,
  ConnectionId,
  Dialogs,
  DialogVariant,
  ValidConfigType,
  ValidModuleConfigType,
  WaypointWithMetadata,
} from "./types.ts";
...
```