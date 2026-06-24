# ImportDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ImportDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 7669 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ImportDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]
- [[apps/web/src/components/UI/Select.tsx.md|apps/web/src/components/UI/Select.tsx]]
- [[apps/web/src/components/UI/Switch.tsx.md|apps/web/src/components/UI/Switch.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { create, fromBinary } from "@bufbuild/protobuf";
import { Button } from "@components/UI/Button.tsx";
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
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@components/UI/Select.tsx";
...
```