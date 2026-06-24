# useUnsafeRolesDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 4477 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Mock`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts.md|apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts]]
- [[apps/web/src/core/utils/eventBus.ts.md|apps/web/src/core/utils/eventBus.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import {
  UNSAFE_ROLES,
  useUnsafeRolesDialog,
} from "@components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts";
import { eventBus } from "@core/utils/eventBus.ts";
import { renderHook } from "@testing-library/react";
import {
  afterEach,
  beforeEach,
  describe,
  expect,
  it,
  type Mock,
  vi,
} from "vitest";

const mockNavigate = vi.fn();
vi.mock("@tanstack/react-router", async (importOriginal) => {
  const actual =
    await importOriginal<typeof import("@tanstack/react-router")>();
...
```