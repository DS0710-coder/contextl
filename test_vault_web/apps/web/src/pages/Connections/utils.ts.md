# utils.ts

## Architecture Metrics
- **Path:** `apps/web/src/pages/Connections/utils.ts`
- **Extension:** `.ts`
- **Size:** 2108 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createConnectionFromInput`
- `connectionTypeIcon`
- `formatConnectionSubtext`

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[apps/web/src/core/utils/randId.ts.md|apps/web/src/core/utils/randId.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/core/connections/transports.ts.md|apps/web/src/core/connections/transports.ts]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import type {
  Connection,
  ConnectionStatus,
  ConnectionType,
  NewConnection,
} from "@app/core/stores/deviceStore/types";
import { randId } from "@app/core/utils/randId";
import { Bluetooth, Cable, Globe, type LucideIcon } from "lucide-react";

export function createConnectionFromInput(input: NewConnection): Connection {
  const base = {
    id: randId(),
    name: input.name,
    createdAt: Date.now(),
    status: "disconnected" as ConnectionStatus,
  };
  if (input.type === "http") {
    return {
      ...base,
      type: "http",
...
```