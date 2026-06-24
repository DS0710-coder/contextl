# DeviceWrapper.tsx

## Architecture Metrics
- **Path:** `apps/web/src/DeviceWrapper.tsx`
- **Extension:** `.tsx`
- **Size:** 387 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceWrapperProps`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/tests/test-utils.tsx.md|apps/web/src/tests/test-utils.tsx]]

## Source Code Snippet
```tsx
import { CurrentDeviceContext } from "@core/stores";
import type { ReactNode } from "react";

export interface DeviceWrapperProps {
  children: ReactNode;
  deviceId: number;
}

export const DeviceWrapper = ({ children, deviceId }: DeviceWrapperProps) => {
  return (
    <CurrentDeviceContext.Provider value={{ deviceId }}>
      {children}
    </CurrentDeviceContext.Provider>
  );
};
```