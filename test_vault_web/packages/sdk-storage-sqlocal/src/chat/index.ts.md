# index.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/chat/index.ts`
- **Extension:** `.ts`
- **Size:** 312 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/mod.ts.md|packages/sdk-storage-sqlocal/mod.ts]]

## Source Code Snippet
```ts
export { SqlocalMessageRepository } from "./SqlocalMessageRepository.ts";
export type { SqlocalMessageRepositoryOptions } from "./SqlocalMessageRepository.ts";
export { SqlocalDraftRepository } from "./SqlocalDraftRepository.ts";
export type { SqlocalDraftRepositoryOptions } from "./SqlocalDraftRepository.ts";
```