# meshRegistry.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/meshRegistry.ts`
- **Extension:** `.ts`
- **Size:** 577 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import { MeshRegistry } from "@meshtastic/sdk";

/**
 * App-wide MeshRegistry singleton.
 *
 * Holds one `MeshClient` per active connection. Wrapped at the root by
 * `<MeshRegistryProvider registry={meshRegistry}>` so descendant components
 * can use `useMeshDevice()`, `useChat()`, etc. against the active client.
 *
 * During Phase B migration the registry coexists with the legacy Zustand
 * deviceStore; `useConnections` continues to instantiate `MeshDevice` (the
 * SDK's Phase-A shim) until per-slice migrations land.
 */
export const meshRegistry = new MeshRegistry();
```