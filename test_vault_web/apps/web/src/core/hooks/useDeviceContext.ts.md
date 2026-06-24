# useDeviceContext.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useDeviceContext.ts`
- **Extension:** `.ts`
- **Size:** 488 bytes
- **Centrality Score:** 0.0032
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceContext`
- `useDeviceContext`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/stores/utils/bindStoreToDevice.ts.md|apps/web/src/core/stores/utils/bindStoreToDevice.ts]]

## Source Code Snippet
```ts
import { createContext, useContext } from "react";

export type DeviceContext = {
  deviceId: number; // Unique identifier for the device, not nodeNum
};

export const CurrentDeviceContext = createContext<DeviceContext | undefined>(
  undefined,
);

export function useDeviceContext(): DeviceContext {
  const ctx = useContext(CurrentDeviceContext);
  if (!ctx) {
    throw new Error(
      "useDeviceContext must be used within CurrentDeviceContext provider",
    );
  }
  return ctx;
}
```