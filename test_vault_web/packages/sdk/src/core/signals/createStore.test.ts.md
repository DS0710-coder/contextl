# createStore.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/signals/createStore.test.ts`
- **Extension:** `.ts`
- **Size:** 1770 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { SignalMap, createStore, toReadonly } from "./createStore.ts";

describe("createStore", () => {
  it("exposes initial value through the readable facade", () => {
    const store = createStore(7);
    expect(store.read.value).toBe(7);
  });

  it("propagates writes to subscribers", () => {
    const store = createStore("a");
    const seen: string[] = [];
    const unsubscribe = store.read.subscribe((v) => seen.push(v));
    store.write.value = "b";
    store.write.value = "c";
    unsubscribe();
    store.write.value = "d";
    expect(seen).toEqual(["b", "c"]);
  });

...
```