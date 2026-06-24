# DeviceImage.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/DeviceImage.tsx`
- **Extension:** `.tsx`
- **Size:** 2074 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceImageProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]

## Source Code Snippet
```tsx
export interface DeviceImageProps {
  deviceType: string;
  className?: React.HTMLAttributes<HTMLImageElement>["className"];
}

const hardwareModelToFilename: { [key: string]: string } = {
  DIY_V1: "diy.svg",
  NANO_G2_ULTRA: "nano-g2-ultra.svg",
  TBEAM: "tbeam.svg",
  HELTEC_HT62: "heltec-ht62-esp32c3-sx1262.svg",
  RPI_PICO: "pico.svg",
  T_DECK: "t-deck.svg",
  HELTEC_MESH_NODE_T114: "heltec-mesh-node-t114.svg",
  HELTEC_MESH_NODE_T114_CASE: "heltec-mesh-node-t114-case.svg",
  HELTEC_V3: "heltec-v3.svg",
  HELTEC_V3_CASE: "heltec-v3-case.svg",
  HELTEC_VISION_MASTER_E213: "heltec-vision-master-e213.svg",
  HELTEC_VISION_MASTER_E290: "heltec-vision-master-e290.svg",
  HELTEC_VISION_MASTER_T190: "heltec-vision-master-t190.svg",
  HELTEC_WIRELESS_PAPER: "heltec-wireless-paper.svg",
...
```