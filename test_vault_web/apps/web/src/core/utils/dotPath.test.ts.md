# dotPath.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/dotPath.test.ts`
- **Extension:** `.ts`
- **Size:** 1740 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/dotPath.ts.md|apps/web/src/core/utils/dotPath.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { dotPaths } from "./dotPath.ts";

describe("dotPaths", () => {
  it("returns flat keys for a simple object", () => {
    const obj = { a: 1, b: 2, c: 3 };
    expect(dotPaths(obj)).toEqual(["a", "b", "c"]);
  });

  it("returns dot notation keys for nested objects", () => {
    const obj = { a: { b: { c: 1 } }, d: 2 };
    expect(dotPaths(obj)).toEqual(["a.b.c", "d"]);
  });

  it("handles arrays at the root", () => {
    const arr = [{ x: 1 }, { y: 2 }];
    expect(dotPaths(arr)).toEqual(["0.x", "1.y"]);
  });

  it("handles arrays nested in objects", () => {
...
```