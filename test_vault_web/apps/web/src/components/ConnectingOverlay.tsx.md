# ConnectingOverlay.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/ConnectingOverlay.tsx`
- **Extension:** `.tsx`
- **Size:** 7121 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChipProps`
- `Chip`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]

## Source Code Snippet
```tsx
import { Dialog, DialogContent, DialogTitle } from "@components/UI/Dialog.tsx";
import { Button } from "@components/UI/Button.tsx";
import { useDeviceStore } from "@core/stores";
import { cn } from "@core/utils/cn.ts";
import { useConnections } from "@app/pages/Connections/useConnections";
import { useConnectionProgress } from "@meshtastic/sdk-react";
import { Bluetooth, Cable, CheckCircle2, Globe, Loader2 } from "lucide-react";
import type { ComponentType, ReactElement } from "react";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";

const STUCK_THRESHOLD_MS = 15_000;

const TRANSPORT_ICON: Record<
  "http" | "bluetooth" | "serial",
  ComponentType<{ className?: string }>
> = {
  http: Globe,
  bluetooth: Bluetooth,
  serial: Cable,
...
```