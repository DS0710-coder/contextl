# QRDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/QRDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 5139 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `QRDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { create, toBinary } from "@bufbuild/protobuf";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { Input } from "@components/UI/Input.tsx";
import { Label } from "@components/UI/Label.tsx";
import { Protobuf } from "@meshtastic/sdk";
import { useChannels } from "@meshtastic/sdk-react";
import { fromByteArray } from "base64-js";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { QRCode } from "react-qrcode-logo";
import { Checkbox } from "../UI/Checkbox/index.tsx";

...
```