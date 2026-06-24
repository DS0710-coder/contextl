# FilesClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/files/FilesClient.ts`
- **Extension:** `.ts`
- **Size:** 2170 bytes
- **Centrality Score:** 0.0025
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilesClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/identifiers/PacketId.ts.md|packages/sdk/src/core/identifiers/PacketId.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/files/domain/FileTransfer.ts.md|packages/sdk/src/features/files/domain/FileTransfer.ts]]
- [[packages/sdk/src/features/files/state/filesStore.ts.md|packages/sdk/src/features/files/state/filesStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/files/index.ts.md|packages/sdk/src/features/files/index.ts]]

## Source Code Snippet
```ts
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import { generatePacketId } from "../../core/identifiers/PacketId.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import type { FileTransfer } from "./domain/FileTransfer.ts";
import { FilesStore } from "./state/filesStore.ts";

export class FilesClient {
  private readonly client: MeshClient;
  private readonly store: FilesStore;
  public readonly transfers: ReadonlySignal<ReadonlyArray<FileTransfer>>;

  constructor(client: MeshClient) {
    this.client = client;
    this.store = new FilesStore();
    this.transfers = this.store.read;
  }

  public async upload(
...
```