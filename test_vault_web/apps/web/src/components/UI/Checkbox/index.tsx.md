# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Checkbox/index.tsx`
- **Extension:** `.tsx`
- **Size:** 2217 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CheckboxProps`
- `Checkbox`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/ManagedModeDialog.tsx.md|apps/web/src/components/Dialog/ManagedModeDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx.md|apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx]]
- [[apps/web/src/components/UI/Checkbox/Checkbox.test.tsx.md|apps/web/src/components/UI/Checkbox/Checkbox.test.tsx]]
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import { Check } from "lucide-react";
import { useId, useState } from "react";

interface CheckboxProps {
  checked?: boolean;
  defaultChecked?: boolean;
  onChange?: (checked: boolean) => void;
  className?: string;
  labelClassName?: string;
  id?: string;
  children?: React.ReactNode;
  disabled?: boolean;
  required?: boolean;
  name?: string;
}

export function Checkbox({
  checked,
  defaultChecked = false,
...
```