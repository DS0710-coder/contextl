# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Nodes/index.tsx`
- **Extension:** `.tsx`
- **Size:** 10248 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 16

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilterState`
- `DataRow`
- `Heading`
- `JSX`
- `DeleteNoteDialogProps`
- `handleNodeInfoDialog`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/LocationResponseDialog.tsx.md|apps/web/src/components/Dialog/LocationResponseDialog.tsx]]
- [[apps/web/src/components/Dialog/TracerouteResponseDialog.tsx.md|apps/web/src/components/Dialog/TracerouteResponseDialog.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[apps/web/src/components/generic/Mono.tsx.md|apps/web/src/components/generic/Mono.tsx]]
- [[apps/web/src/components/generic/Table/index.tsx.md|apps/web/src/components/generic/Table/index.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/core/hooks/useLang.ts.md|apps/web/src/core/hooks/useLang.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import { LocationResponseDialog } from "@app/components/Dialog/LocationResponseDialog.tsx";
import { TracerouteResponseDialog } from "@app/components/Dialog/TracerouteResponseDialog.tsx";
import { FilterControl } from "@components/generic/Filter/FilterControl.tsx";
import {
  type FilterState,
  useFilterNode,
} from "@components/generic/Filter/useFilterNode.ts";
import { Mono } from "@components/generic/Mono.tsx";
import {
  type DataRow,
  type Heading,
  Table,
} from "@components/generic/Table/index.tsx";
import { TimeAgo } from "@components/generic/TimeAgo.tsx";
import { PageLayout } from "@components/PageLayout.tsx";
import { Sidebar } from "@components/Sidebar.tsx";
import { Avatar } from "@components/UI/Avatar.tsx";
import { Input } from "@components/UI/Input.tsx";
import useLang from "@core/hooks/useLang.ts";
import { useNodesAsProto } from "@core/hooks/useNodesAsProto.ts";
...
```