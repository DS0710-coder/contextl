# logger.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/logging/logger.ts`
- **Extension:** `.ts`
- **Size:** 1418 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `defaultMinLevel`
- `createLogger`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
import { Logger } from "tslog";

const prettyLogTemplate =
  "{{hh}}:{{MM}}:{{ss}}:{{ms}}\t{{logLevelName}}\t[{{name}}]\t";

/**
 * Minimum log level. Default is `info` (3). Lifts to `debug` (2) when:
 * - `localStorage["mesh-debug"] === "1"` in a browser context, or
 * - `process.env.MESH_DEBUG === "1"` in a Node / Bun / Deno context.
 *
 * Read once per `createLogger` call so the flag can be flipped at any
 * time and new sub-loggers will pick it up; existing logger instances
 * keep their level unless the caller explicitly resets it.
 */
function defaultMinLevel(): number {
  try {
    if (
      typeof globalThis !== "undefined" &&
      typeof (globalThis as { localStorage?: Storage }).localStorage !==
        "undefined" &&
...
```