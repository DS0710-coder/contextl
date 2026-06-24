# TracerouteResponseDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/TracerouteResponseDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 2300 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TracerouteResponseDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import { useNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import type { Protobuf, Types } from "@meshtastic/sdk";
import { numberToHexUnpadded } from "@noble/curves/utils.js";
import { useTranslation } from "react-i18next";

import { TraceRoute } from "../PageComponents/Messages/TraceRoute.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "../UI/Dialog.tsx";

export interface TracerouteResponseDialogProps {
  traceroute: Types.PacketMetadata<Protobuf.Mesh.RouteDiscovery> | undefined;
  open: boolean;
  onOpenChange: () => void;
}
...
```