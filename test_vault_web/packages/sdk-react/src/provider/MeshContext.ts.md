# MeshContext.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/provider/MeshContext.ts`
- **Extension:** `.ts`
- **Size:** 168 bytes
- **Centrality Score:** 0.0029
- **In-Degree (Imported By):** 3
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
- [[packages/sdk-react/src/provider/MeshProvider.tsx.md|packages/sdk-react/src/provider/MeshProvider.tsx]]

## Source Code Snippet
```ts
import type { MeshClient } from "@meshtastic/sdk";
import { createContext } from "react";

export const MeshContext = createContext<MeshClient | undefined>(undefined);
```