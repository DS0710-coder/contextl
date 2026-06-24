# TraceRoute.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/traceroute/domain/TraceRoute.ts`
- **Extension:** `.ts`
- **Size:** 168 bytes
- **Centrality Score:** 0.0034
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TraceRoute`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/traceroute/TraceRouteClient.ts.md|packages/sdk/src/features/traceroute/TraceRouteClient.ts]]
- [[packages/sdk/src/features/traceroute/index.ts.md|packages/sdk/src/features/traceroute/index.ts]]
- [[packages/sdk/src/features/traceroute/state/tracerouteStore.ts.md|packages/sdk/src/features/traceroute/state/tracerouteStore.ts]]

## Source Code Snippet
```ts
export interface TraceRoute {
  readonly destination: number;
  readonly route: ReadonlyArray<number>;
  readonly snr?: ReadonlyArray<number>;
  readonly time: Date;
}
```