# deepCompareConfig.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/deepCompareConfig.test.ts`
- **Extension:** `.ts`
- **Size:** 4189 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/deepCompareConfig.ts.md|apps/web/src/core/utils/deepCompareConfig.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { deepCompareConfig } from "./deepCompareConfig.ts";

describe("deepCompareConfig", () => {
  it("returns true for identical primitives", () => {
    expect(deepCompareConfig(5, 5)).toBe(true);
    expect(deepCompareConfig("foo", "foo")).toBe(true);
    expect(deepCompareConfig(true, true)).toBe(true);
  });

  it("returns false for different primitives", () => {
    expect(deepCompareConfig(5, 6)).toBe(false);
    expect(deepCompareConfig("foo", "bar")).toBe(false);
    expect(deepCompareConfig(true, false)).toBe(false);
  });

  it("handles nulls correctly", () => {
    expect(deepCompareConfig(null, null)).toBe(true);
    expect(deepCompareConfig(null, undefined)).toBe(false);
    expect(deepCompareConfig(null, {})).toBe(false);
...
```