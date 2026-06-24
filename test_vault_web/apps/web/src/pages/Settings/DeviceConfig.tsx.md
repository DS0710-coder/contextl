# DeviceConfig.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Settings/DeviceConfig.tsx`
- **Extension:** `.tsx`
- **Size:** 3867 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConfigProps`
- `TabItem`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Settings/Bluetooth.tsx.md|apps/web/src/components/PageComponents/Settings/Bluetooth.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Display.tsx.md|apps/web/src/components/PageComponents/Settings/Display.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Power.tsx.md|apps/web/src/components/PageComponents/Settings/Power.tsx]]
- [[apps/web/src/components/PageComponents/Settings/User.tsx.md|apps/web/src/components/PageComponents/Settings/User.tsx]]
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/components/UI/Tabs.tsx.md|apps/web/src/components/UI/Tabs.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { Bluetooth } from "@components/PageComponents/Settings/Bluetooth.tsx";
import { Device } from "@components/PageComponents/Settings/Device/index.tsx";
import { Display } from "@components/PageComponents/Settings/Display.tsx";
import { Network } from "@components/PageComponents/Settings/Network/index.tsx";
import { Position } from "@components/PageComponents/Settings/Position.tsx";
import { Power } from "@components/PageComponents/Settings/Power.tsx";
import { User } from "@components/PageComponents/Settings/User.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@components/UI/Tabs.tsx";
import type { ValidConfigType } from "@core/stores";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { type ComponentType, Suspense, useMemo } from "react";
import type { UseFormReturn } from "react-hook-form";
import { useTranslation } from "react-i18next";

...
```