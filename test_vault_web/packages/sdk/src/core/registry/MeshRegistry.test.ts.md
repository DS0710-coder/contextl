# MeshRegistry.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/registry/MeshRegistry.test.ts`
- **Extension:** `.ts`
- **Size:** 1916 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/registry/MeshRegistry.ts.md|packages/sdk/src/core/registry/MeshRegistry.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { createFakeTransport } from "../testing/createFakeTransport.ts";
import { MeshRegistry } from "./MeshRegistry.ts";

describe("MeshRegistry", () => {
  it("creates clients keyed by id and emits a snapshot", () => {
    const reg = new MeshRegistry();
    const seen: number[] = [];
    reg.list.subscribe((entries) => seen.push(entries.length));

    const { transport: t1 } = createFakeTransport();
    const { transport: t2 } = createFakeTransport();

    reg.create(1, { transport: t1 });
    reg.create(2, { transport: t2 });

    expect(reg.size).toBe(2);
    expect(reg.get(1)).toBeDefined();
    expect(reg.get(42)).toBeUndefined();
    expect(seen).toEqual([1, 2]);
...
```