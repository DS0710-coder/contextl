# types.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/types.ts`
- **Extension:** `.ts`
- **Size:** 92 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceMetrics`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/BatteryStatus.tsx.md|apps/web/src/components/BatteryStatus.tsx]]
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]

## Source Code Snippet
```ts
export type DeviceMetrics = {
  batteryLevel?: number | null;
  voltage?: number | null;
};
```