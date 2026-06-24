# useConnectionProgress.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useConnectionProgress.ts`
- **Extension:** `.ts`
- **Size:** 969 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useConnectionProgress`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ConnectionProgress, ReadonlySignal } from "@meshtastic/sdk";
import { useActiveClient } from "../adapters/useActiveClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

const IDLE_PROGRESS: ConnectionProgress = { phase: "idle" };
const IDLE_SIGNAL: ReadonlySignal<ConnectionProgress> = {
  value: IDLE_PROGRESS,
  peek: () => IDLE_PROGRESS,
  subscribe: () => () => {},
};

/**
 * Live view of `MeshClient.progress` for the active registry client.
 * Returns `{ phase: "idle" }` when no client is active or before
 * `configure()` runs; flips through `configuring` (with per-section
 * counters) and lands on `configured` once the device finishes streaming
 * its config bundle. UI surfaces use this to drive a connecting overlay
 * with live "received N nodes / X channels" feedback.
 */
export function useConnectionProgress(): ConnectionProgress {
...
```