# FileTransfer.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/files/domain/FileTransfer.ts`
- **Extension:** `.ts`
- **Size:** 273 bytes
- **Centrality Score:** 0.0034
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TransferStatus`
- `FileTransfer`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]
- [[packages/sdk/src/features/files/index.ts.md|packages/sdk/src/features/files/index.ts]]
- [[packages/sdk/src/features/files/state/filesStore.ts.md|packages/sdk/src/features/files/state/filesStore.ts]]

## Source Code Snippet
```ts
export type TransferStatus = "pending" | "in_progress" | "complete" | "failed";

export interface FileTransfer {
  readonly id: number;
  readonly filename: string;
  readonly direction: "upload" | "download";
  readonly status: TransferStatus;
  readonly size?: number;
}
```