# filesStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/files/state/filesStore.ts`
- **Extension:** `.ts`
- **Size:** 197 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilesStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/files/domain/FileTransfer.ts.md|packages/sdk/src/features/files/domain/FileTransfer.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { FileTransfer } from "../domain/FileTransfer.ts";

export class FilesStore extends SignalMap<number, FileTransfer> {}
```