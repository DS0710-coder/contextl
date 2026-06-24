# mod.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/mod.ts`
- **Extension:** `.ts`
- **Size:** 828 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/chat/index.ts.md|packages/sdk-storage-sqlocal/src/chat/index.ts]]
- [[packages/sdk-storage-sqlocal/src/coordination/index.ts.md|packages/sdk-storage-sqlocal/src/coordination/index.ts]]
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/index.ts.md|packages/sdk-storage-sqlocal/src/nodes/index.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/index.ts.md|packages/sdk-storage-sqlocal/src/telemetry/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/sdkStorage.ts.md|apps/web/src/core/sdkStorage.ts]]

## Source Code Snippet
```ts
export { createSqlocalDb } from "./src/db.ts";
export type { CreateSqlocalDbOptions, SqlocalDb } from "./src/db.ts";
export { MultiTabCoordinator } from "./src/coordination/index.ts";
export type { ChangeEvent, ChangeKind } from "./src/coordination/index.ts";
export { SqlocalMessageRepository } from "./src/chat/index.ts";
export type { SqlocalMessageRepositoryOptions } from "./src/chat/index.ts";
export { SqlocalDraftRepository } from "./src/chat/index.ts";
export type { SqlocalDraftRepositoryOptions } from "./src/chat/index.ts";
export { SqlocalNodesRepository } from "./src/nodes/index.ts";
export type { SqlocalNodesRepositoryOptions } from "./src/nodes/index.ts";
export { SqlocalTelemetryRepository } from "./src/telemetry/index.ts";
export type { SqlocalTelemetryRepositoryOptions } from "./src/telemetry/index.ts";
```