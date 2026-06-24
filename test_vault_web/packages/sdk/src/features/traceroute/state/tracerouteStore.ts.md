# tracerouteStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/traceroute/state/tracerouteStore.ts`
- **Extension:** `.ts`
- **Size:** 196 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TraceRouteStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/traceroute/domain/TraceRoute.ts.md|packages/sdk/src/features/traceroute/domain/TraceRoute.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/traceroute/TraceRouteClient.ts.md|packages/sdk/src/features/traceroute/TraceRouteClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { TraceRoute } from "../domain/TraceRoute.ts";

export class TraceRouteStore extends SignalMap<number, TraceRoute> {}
```