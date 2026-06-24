# useFileTransfer.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useFileTransfer.ts`
- **Extension:** `.ts`
- **Size:** 303 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useFileTransfer`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { FileTransfer } from "@meshtastic/sdk";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export function useFileTransfer(): ReadonlyArray<FileTransfer> {
  const client = useClient();
  return useSignal(client.files.transfers);
}
```