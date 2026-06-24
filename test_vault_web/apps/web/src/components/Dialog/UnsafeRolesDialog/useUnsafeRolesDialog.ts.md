# useUnsafeRolesDialog.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts`
- **Extension:** `.ts`
- **Size:** 1149 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UnsafeRole`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/eventBus.ts.md|apps/web/src/core/utils/eventBus.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.test.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.test.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]

## Source Code Snippet
```ts
import { useDevice } from "@core/stores";
import { eventBus } from "@core/utils/eventBus.ts";
import { useCallback } from "react";

export const UNSAFE_ROLES = ["ROUTER", "ROUTER_LATE", "REPEATER"];
export type UnsafeRole = (typeof UNSAFE_ROLES)[number];

export const useUnsafeRolesDialog = () => {
  const { setDialogOpen } = useDevice();

  const handleCloseDialog = useCallback(() => {
    setDialogOpen("unsafeRoles", false);
  }, [setDialogOpen]);

  const validateRoleSelection = useCallback(
    (newRoleKey: string): Promise<boolean> => {
      if (!UNSAFE_ROLES.includes(newRoleKey as UnsafeRole)) {
        return Promise.resolve(true);
      }

...
```