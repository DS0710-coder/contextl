# useNodesLegacy.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useNodesLegacy.ts`
- **Extension:** `.ts`
- **Size:** 2056 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useNodesAsProto`
- `useNodeAsProto`
- `useMyNodeAsProto`
- `toNodeInfo`

## Imports (Dependencies)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import type { Node as SdkNode } from "@meshtastic/sdk";
import { Protobuf } from "@meshtastic/sdk";
import { useMeshDevice, useNodes } from "@meshtastic/sdk-react";
import { useMemo } from "react";

/**
 * Adapter hooks that surface SDK-managed nodes in the legacy
 * `Protobuf.Mesh.NodeInfo` shape consumed by web components today.
 *
 * Lets components migrate off the Zustand `useNodeDB().getNodes/getNode`
 * API one at a time without rewriting their templates. Removed once
 * every consumer reads `Node` from the SDK directly.
 */

export function useNodesAsProto(): Protobuf.Mesh.NodeInfo[] {
  const nodes = useNodes();
  return useMemo(() => nodes.map(toNodeInfo), [nodes]);
}

...
```