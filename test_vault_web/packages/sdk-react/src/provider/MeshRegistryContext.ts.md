# MeshRegistryContext.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/provider/MeshRegistryContext.ts`
- **Extension:** `.ts`
- **Size:** 185 bytes
- **Centrality Score:** 0.0039
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useMeshRegistry.ts.md|packages/sdk-react/src/adapters/useMeshRegistry.ts]]
- [[packages/sdk-react/src/provider/MeshRegistryProvider.tsx.md|packages/sdk-react/src/provider/MeshRegistryProvider.tsx]]

## Source Code Snippet
```ts
import type { MeshRegistry } from "@meshtastic/sdk";
import { createContext } from "react";

export const MeshRegistryContext = createContext<MeshRegistry | undefined>(
  undefined,
);
```