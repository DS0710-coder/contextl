# transport.test.ts

## Architecture Metrics
- **Path:** `packages/transport-web-bluetooth/src/transport.test.ts`
- **Extension:** `.ts`
- **Size:** 6205 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MiniEmitter`
- `stubWebBluetooth`

## Imports (Dependencies)
- [[packages/transport-web-bluetooth/src/transport.ts.md|packages/transport-web-bluetooth/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, vi } from "vitest";
import { runTransportContract } from "../../../tests/utils/transportContract.ts";
import { TransportWebBluetooth } from "./transport.ts";

class MiniEmitter {
  private listeners = new Map<string, Set<(e: Event) => void>>();
  addEventListener(type: string, listener: (e: Event) => void) {
    if (!this.listeners.has(type)) {
      this.listeners.set(type, new Set());
    }
    this.listeners.get(type)!.add(listener);
  }
  removeEventListener(type: string, listener: (e: Event) => void) {
    this.listeners.get(type)?.delete(listener);
  }
  dispatchEvent(event: Event) {
    this.listeners.get(event.type)?.forEach((l) => {
      l(event);
    });
  }
...
```