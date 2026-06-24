# appStore.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/appStore/appStore.test.ts`
- **Extension:** `.ts`
- **Size:** 5346 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeRaster`

## Imports (Dependencies)
- [[apps/web/src/core/stores/appStore/index.ts.md|apps/web/src/core/stores/appStore/index.ts]]
- [[apps/web/src/core/stores/appStore/types.ts.md|apps/web/src/core/stores/appStore/types.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { RasterSource } from "@core/stores/appStore/types.ts";
import { beforeEach, describe, expect, it, vi } from "vitest";

const idbMem = new Map<string, string>();
vi.mock("idb-keyval", () => ({
  get: vi.fn((key: string) => Promise.resolve(idbMem.get(key))),
  set: vi.fn((key: string, val: string) => {
    idbMem.set(key, val);
    return Promise.resolve();
  }),
  del: vi.fn((key: string) => {
    idbMem.delete(key);
    return Promise.resolve();
  }),
}));

async function freshStore(persistApp = false) {
  vi.resetModules();

  vi.spyOn(console, "debug").mockImplementation(() => {});
...
```