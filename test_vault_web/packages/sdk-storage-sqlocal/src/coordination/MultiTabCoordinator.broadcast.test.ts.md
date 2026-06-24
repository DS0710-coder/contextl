# MultiTabCoordinator.broadcast.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.broadcast.test.ts`
- **Extension:** `.ts`
- **Size:** 1095 bytes
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
import { describe, expect, it } from "vitest";
import { MultiTabCoordinator } from "./MultiTabCoordinator.ts";

/**
 * Node 19+ exposes a global BroadcastChannel that respects the WHATWG
 * spec for cross-context messaging. We instantiate two coordinators in
 * the same process to simulate two browser tabs.
 */
describe("MultiTabCoordinator broadcast", () => {
  it("delivers events between two coordinator instances", async () => {
    if (typeof BroadcastChannel === "undefined") {
      console.warn("BroadcastChannel unavailable; skipping cross-tab test");
      return;
    }
    const a = new MultiTabCoordinator();
    const b = new MultiTabCoordinator();
    try {
      const received = new Promise<unknown>((resolve) => {
        b.subscribe((event) => resolve(event));
      });
...
```