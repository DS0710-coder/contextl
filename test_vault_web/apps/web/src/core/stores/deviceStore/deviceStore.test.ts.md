# deviceStore.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/deviceStore/deviceStore.test.ts`
- **Extension:** `.ts`
- **Size:** 11510 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeHardware`
- `makeRoute`
- `makeWaypoint`
- `makeAdminMessage`

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import { Protobuf, type Types } from "@meshtastic/sdk";
import { beforeEach, describe, expect, it, vi } from "vitest";

const idbMem = new Map<string, string>();
vi.mock("idb-keyval", () => ({
  get: vi.fn((key: string) => Promise.resolve(idbMem.get(key))),
  set: vi.fn((key: string, val: string) => {
    idbMem.set(key, val);
    return Promise.resolve();
  }),
  del: vi.fn((k: string) => {
    idbMem.delete(k);
    return Promise.resolve();
  }),
}));

// Helper to load a fresh copy of the store with persist flag on/off
async function freshStore(persist = false) {
  vi.resetModules();
...
```