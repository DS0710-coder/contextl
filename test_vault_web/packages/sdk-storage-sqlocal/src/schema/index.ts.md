# index.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/index.ts`
- **Extension:** `.ts`
- **Size:** 149 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/schema/chat.ts.md|packages/sdk-storage-sqlocal/src/schema/chat.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/drafts.ts.md|packages/sdk-storage-sqlocal/src/schema/drafts.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/migrations.ts.md|packages/sdk-storage-sqlocal/src/schema/migrations.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/nodes.ts.md|packages/sdk-storage-sqlocal/src/schema/nodes.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/telemetry.ts.md|packages/sdk-storage-sqlocal/src/schema/telemetry.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
export * from "./chat.ts";
export * from "./drafts.ts";
export * from "./nodes.ts";
export * from "./telemetry.ts";
export * from "./migrations.ts";
```