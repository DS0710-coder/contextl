# indexDB.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/utils/indexDB.test.ts`
- **Extension:** `.ts`
- **Size:** 5793 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PersistStorage`

## Imports (Dependencies)
- [[apps/web/src/core/stores/utils/indexDB.ts.md|apps/web/src/core/stores/utils/indexDB.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import * as idb from "idb-keyval";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { createStorage } from "./indexDB.ts";

type PersistStorage<T> = ReturnType<typeof createStorage<T>>;

describe("indexDB.ts persistence (steps 1–5)", () => {
  let store: PersistStorage<any>;

  beforeEach(() => {
    vi.restoreAllMocks();
    store = createStorage<any>();
  });

  async function roundTrip(obj: any) {
    const setSpy = vi.spyOn(idb, "set").mockResolvedValue();
    const getSpy = vi.spyOn(idb, "get");
    await store.setItem("rt", obj);
    const storedStr = (setSpy.mock.calls[0] as any[])[1] as string;
    getSpy.mockResolvedValue(storedStr);
...
```