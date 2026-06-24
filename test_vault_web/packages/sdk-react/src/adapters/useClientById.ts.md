# useClientById.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useClientById.ts`
- **Extension:** `.ts`
- **Size:** 359 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useClientById`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useMeshRegistry.ts.md|packages/sdk-react/src/adapters/useMeshRegistry.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ConnectionId, MeshClient } from "@meshtastic/sdk";
import { useMeshRegistry } from "./useMeshRegistry.ts";

export function useClientById(id: ConnectionId): MeshClient {
  const registry = useMeshRegistry();
  const client = registry.get(id);
  if (!client) {
    throw new Error(`No MeshClient registered for id ${id}`);
  }
  return client;
}
```