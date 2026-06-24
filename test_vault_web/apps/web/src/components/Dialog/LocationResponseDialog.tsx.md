# LocationResponseDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/LocationResponseDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 2998 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LocationResponseDialogProps`

## Imports (Dependencies)
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
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "../UI/Dialog.tsx";

export interface LocationResponseDialogProps {
  location: Types.PacketMetadata<Protobuf.Mesh.Position> | undefined;
  open: boolean;
  onOpenChange: () => void;
}

export const LocationResponseDialog = ({
...
```