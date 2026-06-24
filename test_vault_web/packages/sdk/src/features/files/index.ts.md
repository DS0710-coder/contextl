# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/files/index.ts`
- **Extension:** `.ts`
- **Size:** 126 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]
- [[packages/sdk/src/features/files/domain/FileTransfer.ts.md|packages/sdk/src/features/files/domain/FileTransfer.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { FilesClient } from "./FilesClient.ts";
export type { FileTransfer, TransferStatus } from "./domain/FileTransfer.ts";
```