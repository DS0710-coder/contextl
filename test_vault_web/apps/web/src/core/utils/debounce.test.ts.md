# debounce.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/debounce.test.ts`
- **Extension:** `.ts`
- **Size:** 1742 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/debounce.ts.md|apps/web/src/core/utils/debounce.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { debounce } from "./debounce.ts";

describe("debounce", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it("delays executing the callback until after wait time has elapsed", () => {
    const mockCallback = vi.fn();
    const debouncedFunction = debounce(mockCallback, 500);

    debouncedFunction();
    expect(mockCallback).not.toHaveBeenCalled();

    vi.advanceTimersByTime(300);
...
```