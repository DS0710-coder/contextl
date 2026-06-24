# randId.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/randId.test.ts`
- **Extension:** `.ts`
- **Size:** 1116 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/randId.ts.md|apps/web/src/core/utils/randId.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { beforeEach, describe, expect, it, vi } from "vitest";
import { randId } from "./randId.ts";

describe("randId", () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it("returns a number", () => {
    const result = randId();
    expect(typeof result).toBe("number");
  });

  it("returns an integer", () => {
    const result = randId();
    expect(Number.isInteger(result)).toBe(true);
  });

  it("uses Math.random to generate the number", () => {
    const mockRandom = vi.spyOn(Math, "random").mockReturnValue(0.5);
...
```