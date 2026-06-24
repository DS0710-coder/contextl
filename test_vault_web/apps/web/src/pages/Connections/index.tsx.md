# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Connections/index.tsx`
- **Extension:** `.tsx`
- **Size:** 14351 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TypeBadge`
- `ConnectionCard`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx.md|apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx]]
- [[apps/web/src/components/UI/AlertDialog.tsx.md|apps/web/src/components/UI/AlertDialog.tsx]]
- [[apps/web/src/components/UI/Badge.tsx.md|apps/web/src/components/UI/Badge.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Card.tsx.md|apps/web/src/components/UI/Card.tsx]]
- [[apps/web/src/components/UI/DropdownMenu.tsx.md|apps/web/src/components/UI/DropdownMenu.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import AddConnectionDialog from "@app/components/Dialog/AddConnectionDialog/AddConnectionDialog";
import { TimeAgo } from "@app/components/generic/TimeAgo";
import LanguageSwitcher from "@app/components/LanguageSwitcher";
import { ConnectionStatusBadge } from "@app/components/PageComponents/Connections/ConnectionStatusBadge";
import type { Connection } from "@app/core/stores/deviceStore/types";
import { useConnections } from "@app/pages/Connections/useConnections";
import {
  connectionTypeIcon,
  formatConnectionSubtext,
} from "@app/pages/Connections/utils";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
...
```