# ConnectionStatusBadge.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx`
- **Extension:** `.tsx`
- **Size:** 991 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConnectionStatusBadge`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@app/components/UI/Button";
import type { Connection } from "@app/core/stores/deviceStore/types";

export function ConnectionStatusBadge({
  status,
}: {
  status: Connection["status"];
}) {
  let color = "";
  let displayStatus = status;

  switch (status) {
    case "connected":
    case "configured":
      color = "bg-emerald-500";
      displayStatus = "connected";
      break;
    case "connecting":
    case "configuring":
      color = "bg-amber-500";
...
```