# MultiTabCoordinator.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.test.ts`
- **Extension:** `.ts`
- **Size:** 816 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.ts.md|packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it, vi } from "vitest";
import { MultiTabCoordinator } from "./MultiTabCoordinator.ts";

describe("MultiTabCoordinator", () => {
  it("falls through acquireLock when navigator.locks is unavailable", async () => {
    const coordinator = new MultiTabCoordinator();
    const handler = vi.fn().mockResolvedValue(42);
    const result = await coordinator.acquireLock("res", handler);
    expect(result).toBe(42);
    expect(handler).toHaveBeenCalledTimes(1);
  });

  it("subscribe/unsubscribe gates listeners", () => {
    const coordinator = new MultiTabCoordinator();
    const seen: number[] = [];
    const off = coordinator.subscribe(() => seen.push(1));
    off();
    // No real BroadcastChannel here; ensure subscribe returns a callable no-op
    expect(seen).toEqual([]);
  });
...
```