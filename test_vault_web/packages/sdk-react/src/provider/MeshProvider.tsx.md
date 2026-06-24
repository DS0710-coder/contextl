# MeshProvider.tsx

## Architecture Metrics
- **Path:** `packages/sdk-react/src/provider/MeshProvider.tsx`
- **Extension:** `.tsx`
- **Size:** 380 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MeshProviderProps`
- `MeshProvider`

## Imports (Dependencies)
- [[packages/sdk-react/src/provider/MeshContext.ts.md|packages/sdk-react/src/provider/MeshContext.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```tsx
import type { MeshClient } from "@meshtastic/sdk";
import type { ReactNode } from "react";
import { MeshContext } from "./MeshContext.ts";

export interface MeshProviderProps {
  client: MeshClient;
  children: ReactNode;
}

export function MeshProvider({ client, children }: MeshProviderProps) {
  return <MeshContext.Provider value={client}>{children}</MeshContext.Provider>;
}
```