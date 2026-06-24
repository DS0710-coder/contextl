# useNodesAsProto.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useNodesAsProto.ts`
- **Extension:** `.ts`
- **Size:** 2948 bytes
- **Centrality Score:** 0.0034
- **In-Degree (Imported By):** 18
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useSdkNodesSafe`
- `useMyNodeNumSafe`
- `useNodesAsProto`
- `useNodeAsProto`
- `useMyNodeAsProto`
- `toNodeInfo`

## Imports (Dependencies)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]
- [[apps/web/src/components/Dialog/LocationResponseDialog.tsx.md|apps/web/src/components/Dialog/LocationResponseDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/PKIBackupDialog.tsx.md|apps/web/src/components/Dialog/PKIBackupDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/RemoveNodeDialog.tsx.md|apps/web/src/components/Dialog/RemoveNodeDialog.tsx]]
- [[apps/web/src/components/Dialog/TracerouteResponseDialog.tsx.md|apps/web/src/components/Dialog/TracerouteResponseDialog.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx]]
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/PageComponents/Settings/User.tsx.md|apps/web/src/components/PageComponents/Settings/User.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import type { Node as SdkNode } from "@meshtastic/sdk";
import { Protobuf } from "@meshtastic/sdk";
import { useActiveClient, useSignal } from "@meshtastic/sdk-react";
import { useMemo } from "react";

/**
 * Adapter hooks that surface SDK-managed nodes in the
 * `Protobuf.Mesh.NodeInfo` shape consumed by web components today.
 *
 * Wraps the SDK Node into the legacy proto shape so the existing
 * components keep working without rewrites. Removed once every consumer
 * reads `Node` from the SDK directly.
 *
 * Reads through `useActiveClient()` so that, when no client is active
 * (e.g. inside isolated component tests or before any device connects),
 * the hooks return safe empty values instead of throwing.
 */

const EMPTY_NODES: ReadonlyArray<SdkNode> = [];
...
```