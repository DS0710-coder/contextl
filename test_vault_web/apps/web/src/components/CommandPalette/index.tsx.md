# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/CommandPalette/index.tsx`
- **Extension:** `.tsx`
- **Size:** 9339 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LucideIcon`
- `Group`
- `Command`
- `SubItem`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Command.tsx.md|apps/web/src/components/UI/Command.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/usePinnedItems.ts.md|apps/web/src/core/hooks/usePinnedItems.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]

## Source Code Snippet
```tsx
import { Avatar } from "@components/UI/Avatar.tsx";
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@components/UI/Command.tsx";
import { usePinnedItems } from "@core/hooks/usePinnedItems.ts";
import { useNodesAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useAppStore, useDevice, useDeviceStore } from "@core/stores";
import { cn } from "@core/utils/cn.ts";
import { useNavigate } from "@tanstack/react-router";
import { useCommandState } from "cmdk";
import {
  ArrowLeftRightIcon,
  BoxSelectIcon,
  BugIcon,
  CloudOff,
...
```