# signalColor.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/signalColor.ts`
- **Extension:** `.ts`
- **Size:** 564 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]

## Source Code Snippet
```ts
export const SNR_THRESHOLD = {
  GOOD: -7,
  FAIR: -15,
};

export const RSSI_THRESHOLD = {
  GOOD: -115,
  FAIR: -126,
};

export const LINE_COLOR = {
  GOOD: "#00ff00",
  FAIR: "#ffe600",
  BAD: "#f7931a",
};

export const getSignalColor = (snr: number, rssi?: number): string => {
  if (
    snr > SNR_THRESHOLD.GOOD &&
    (rssi == null || rssi > RSSI_THRESHOLD.GOOD)
...
```