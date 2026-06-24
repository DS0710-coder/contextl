# useMeshRegistry.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useMeshRegistry.ts`
- **Extension:** `.ts`
- **Size:** 526 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useMeshRegistry`
- `useOptionalMeshRegistry`

## Imports (Dependencies)
- [[packages/sdk-react/src/provider/MeshRegistryContext.ts.md|packages/sdk-react/src/provider/MeshRegistryContext.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useClientById.ts.md|packages/sdk-react/src/adapters/useClientById.ts]]

## Source Code Snippet
```ts
import type { MeshRegistry } from "@meshtastic/sdk";
import { useContext } from "react";
import { MeshRegistryContext } from "../provider/MeshRegistryContext.ts";

export function useMeshRegistry(): MeshRegistry {
  const registry = useContext(MeshRegistryContext);
  if (!registry) {
    throw new Error(
      "useMeshRegistry must be called inside a <MeshRegistryProvider>.",
    );
  }
  return registry;
}

export function useOptionalMeshRegistry(): MeshRegistry | undefined {
  return useContext(MeshRegistryContext);
}
```