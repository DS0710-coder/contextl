# SupportedBadge.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Badge/SupportedBadge.tsx`
- **Extension:** `.tsx`
- **Size:** 420 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SupportBadge`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Badge.tsx.md|apps/web/src/components/UI/Badge.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]

## Source Code Snippet
```tsx
import { Badge } from "../UI/Badge.tsx";

export function SupportBadge({
  supported,
  labelSupported,
  labelUnsupported,
}: {
  supported: boolean;
  labelSupported: string;
  labelUnsupported: string;
}) {
  return (
    <div className="flex items-center gap-2">
      <Badge variant={supported ? "secondary" : "destructive"}>
        {supported ? labelSupported : labelUnsupported}
      </Badge>
    </div>
  );
}
```