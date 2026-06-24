# types-namespace.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/types-namespace.ts`
- **Extension:** `.ts`
- **Size:** 374 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
Wrapper that surfaces the cross-cutting types under a single namespace
via `import * as Types`. Required because tsdown's dts emitter mishandles
`export * as Types from ...` directly (it emits a reference to a synthetic
`types_d_exports` identifier that's never declared, breaking downstream
consumers' dts bundlers).

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
/**
 * Wrapper that surfaces the cross-cutting types under a single namespace
 * via `import * as Types`. Required because tsdown's dts emitter mishandles
 * `export * as Types from ...` directly (it emits a reference to a synthetic
 * `types_d_exports` identifier that's never declared, breaking downstream
 * consumers' dts bundlers).
 */
export * from "./core/types.ts";
```