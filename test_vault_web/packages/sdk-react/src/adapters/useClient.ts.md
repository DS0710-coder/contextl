# useClient.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useClient.ts`
- **Extension:** `.ts`
- **Size:** 1052 bytes
- **Centrality Score:** 0.0065
- **In-Degree (Imported By):** 15
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useClient`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk-react/src/provider/MeshContext.ts.md|packages/sdk-react/src/provider/MeshContext.ts]]
- [[packages/sdk-react/src/provider/MeshRegistryContext.ts.md|packages/sdk-react/src/provider/MeshRegistryContext.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/hooks/useChat.ts.md|packages/sdk-react/src/hooks/useChat.ts]]
- [[packages/sdk-react/src/hooks/useConfig.ts.md|packages/sdk-react/src/hooks/useConfig.ts]]
- [[packages/sdk-react/src/hooks/useConnection.ts.md|packages/sdk-react/src/hooks/useConnection.ts]]
- [[packages/sdk-react/src/hooks/useDirectChat.ts.md|packages/sdk-react/src/hooks/useDirectChat.ts]]
- [[packages/sdk-react/src/hooks/useDraft.ts.md|packages/sdk-react/src/hooks/useDraft.ts]]
- [[packages/sdk-react/src/hooks/useFavoriteNode.ts.md|packages/sdk-react/src/hooks/useFavoriteNode.ts]]
- [[packages/sdk-react/src/hooks/useFileTransfer.ts.md|packages/sdk-react/src/hooks/useFileTransfer.ts]]
- [[packages/sdk-react/src/hooks/useIgnoreNode.ts.md|packages/sdk-react/src/hooks/useIgnoreNode.ts]]
- [[packages/sdk-react/src/hooks/useMeshDevice.ts.md|packages/sdk-react/src/hooks/useMeshDevice.ts]]
- [[packages/sdk-react/src/hooks/useNode.ts.md|packages/sdk-react/src/hooks/useNode.ts]]
- [[packages/sdk-react/src/hooks/useNodes.ts.md|packages/sdk-react/src/hooks/useNodes.ts]]
- [[packages/sdk-react/src/hooks/usePosition.ts.md|packages/sdk-react/src/hooks/usePosition.ts]]
- [[packages/sdk-react/src/hooks/useTelemetry.ts.md|packages/sdk-react/src/hooks/useTelemetry.ts]]
- [[packages/sdk-react/src/hooks/useTraceroute.ts.md|packages/sdk-react/src/hooks/useTraceroute.ts]]

## Source Code Snippet
```ts
import type { MeshClient } from "@meshtastic/sdk";
import { useContext } from "react";
import { MeshContext } from "../provider/MeshContext.ts";
import { MeshRegistryContext } from "../provider/MeshRegistryContext.ts";
import { useSignal } from "./useSignal.ts";

/**
 * Returns the `MeshClient` for the current tree. Resolves in this order:
 *   1. The nearest `<MeshProvider client={...}>`.
 *   2. The active client of the nearest `<MeshRegistryProvider registry={...}>`.
 *
 * Throws if neither is present or the registry has no active client.
 */
export function useClient(): MeshClient {
  const direct = useContext(MeshContext);
  const registry = useContext(MeshRegistryContext);
  const active = useSignal(
    registry?.active ?? {
      value: undefined,
      peek: () => undefined,
...
```