# EventBus.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/event-bus/EventBus.test.ts`
- **Extension:** `.ts`
- **Size:** 1147 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { EventBus } from "./EventBus.ts";

describe("EventBus", () => {
  it("delivers dispatched payloads to subscribers", () => {
    const bus = new EventBus();
    const received: number[] = [];
    bus.onConfigComplete.subscribe((id) => received.push(id));
    bus.onConfigComplete.dispatch(42);
    bus.onConfigComplete.dispatch(43);
    expect(received).toEqual([42, 43]);
  });

  it("unsubscribe stops future delivery", () => {
    const bus = new EventBus();
    const received: number[] = [];
    const unsub = bus.onConfigComplete.subscribe((id) => received.push(id));
    bus.onConfigComplete.dispatch(1);
    unsub();
    bus.onConfigComplete.dispatch(2);
...
```