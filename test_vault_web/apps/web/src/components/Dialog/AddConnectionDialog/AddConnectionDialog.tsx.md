# AddConnectionDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 22163 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BrowserFeature`
- `LucideIcon`
- `TabKey`
- `TestingStatus`
- `DialogState`
- `DialogAction`
- `FeatureErrorProps`
- `Pane`
- `dialogReducer`
- `PickerRow`

## Imports (Dependencies)
- [[apps/web/src/components/Badge/SupportedBadge.tsx.md|apps/web/src/components/Badge/SupportedBadge.tsx]]
- [[apps/web/src/components/Dialog/AddConnectionDialog/validation.ts.md|apps/web/src/components/Dialog/AddConnectionDialog/validation.ts]]
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]
- [[apps/web/src/components/UI/Switch.tsx.md|apps/web/src/components/UI/Switch.tsx]]
- [[apps/web/src/components/UI/Tabs.tsx.md|apps/web/src/components/UI/Tabs.tsx]]
- [[apps/web/src/components/UI/Typography/Link.tsx.md|apps/web/src/components/UI/Typography/Link.tsx]]
- [[apps/web/src/core/hooks/useBrowserFeatureDetection.ts.md|apps/web/src/core/hooks/useBrowserFeatureDetection.ts]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]
- [[packages/transport-web-bluetooth/mod.ts.md|packages/transport-web-bluetooth/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { SupportBadge } from "@app/components/Badge/SupportedBadge.tsx";
import { Switch } from "@app/components/UI/Switch.tsx";
import type {
  ConnectionType,
  NewConnection,
} from "@app/core/stores/deviceStore/types.ts";
import { testHttpReachable } from "@app/pages/Connections/utils";
import { Button } from "@components/UI/Button.tsx";
import { Input } from "@components/UI/Input.tsx";
import { Label } from "@components/UI/Label.tsx";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@components/UI/Tabs.tsx";
import { Link } from "@components/UI/Typography/Link.tsx";
import {
  type BrowserFeature,
  useBrowserFeatureDetection,
...
```