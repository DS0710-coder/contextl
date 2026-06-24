# MeshRegistryProvider.tsx

## Architecture Metrics
- **Path:** `packages/sdk-react/src/provider/MeshRegistryProvider.tsx`
- **Extension:** `.tsx`
- **Size:** 669 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MeshRegistryProviderProps`
- `MeshRegistryProvider`

## Imports (Dependencies)
- [[packages/sdk-react/src/provider/MeshRegistryContext.ts.md|packages/sdk-react/src/provider/MeshRegistryContext.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```tsx
import type { MeshRegistry } from "@meshtastic/sdk";
import type { ReactNode } from "react";
import { MeshRegistryContext } from "./MeshRegistryContext.ts";

export interface MeshRegistryProviderProps {
  registry: MeshRegistry;
  children: ReactNode;
}

/**
 * Makes a MeshRegistry available to descendant hooks. Use when the app holds
 * more than one connected device at a time. For single-client apps, prefer
 * `<MeshProvider client={...}>`.
 */
export function MeshRegistryProvider({
  registry,
  children,
}: MeshRegistryProviderProps) {
  return (
    <MeshRegistryContext.Provider value={registry}>
...
```