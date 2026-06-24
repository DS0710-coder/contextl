# DisconnectUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/application/DisconnectUseCase.ts`
- **Extension:** `.ts`
- **Size:** 172 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { MeshClient } from "../../../core/client/MeshClient.ts";

export async function disconnect(client: MeshClient): Promise<void> {
  await client.disconnect();
}
```