# eventBus.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/eventBus.test.ts`
- **Extension:** `.ts`
- **Size:** 2451 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/eventBus.ts.md|apps/web/src/core/utils/eventBus.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { eventBus } from "@core/utils/eventBus.ts";
import { beforeEach, describe, expect, it, vi } from "vitest";

describe("EventBus", () => {
  beforeEach(() => {
    // Reset event listeners before each test
    eventBus.offAll();
  });

  it("should register an event listener and trigger it on emit", () => {
    const mockCallback = vi.fn();

    eventBus.on("dialog:unsafeRoles", mockCallback);
    eventBus.emit("dialog:unsafeRoles", { action: "confirm" });

    expect(mockCallback).toHaveBeenCalledWith({ action: "confirm" });
  });

  it("should remove an event listener with off", () => {
    const mockCallback = vi.fn();
...
```