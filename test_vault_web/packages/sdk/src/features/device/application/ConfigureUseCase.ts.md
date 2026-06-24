# ConfigureUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/application/ConfigureUseCase.ts`
- **Extension:** `.ts`
- **Size:** 409 bytes
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

/**
 * Kicks off the wantConfigId handshake. The bulk of configuration state is
 * filled asynchronously as the device streams back FromRadio packets —
 * ConfigClient/NodesClient/ChannelsClient populate their stores from events.
 */
export async function configure(client: MeshClient): Promise<number> {
  return client.configure();
}
```