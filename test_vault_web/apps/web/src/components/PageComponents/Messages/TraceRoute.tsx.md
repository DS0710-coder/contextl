# TraceRoute.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/TraceRoute.tsx`
- **Extension:** `.tsx`
- **Size:** 2141 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeUser`
- `TraceRouteProps`
- `RoutePathProps`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/TracerouteResponseDialog.tsx.md|apps/web/src/components/Dialog/TracerouteResponseDialog.tsx]]
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx]]

## Source Code Snippet
```tsx
import { useNodesAsProto } from "@core/hooks/useNodesAsProto.ts";
import type { Protobuf } from "@meshtastic/sdk";
import { numberToHexUnpadded } from "@noble/curves/utils.js";
import { useTranslation } from "react-i18next";

type NodeUser = Pick<Protobuf.Mesh.NodeInfo, "user">;

export interface TraceRouteProps {
  from: NodeUser;
  to: NodeUser;
  route: Array<number>;
  routeBack?: Array<number>;
  snrTowards?: Array<number>;
  snrBack?: Array<number>;
}

interface RoutePathProps {
  title: string;
  from: NodeUser;
  to: NodeUser;
...
```