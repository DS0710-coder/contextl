# useFilterNode.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Filter/useFilterNode.ts`
- **Extension:** `.ts`
- **Size:** 7764 bytes
- **Centrality Score:** 0.0013
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilterState`
- `useFilterNode`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.test.ts.md|apps/web/src/components/generic/Filter/useFilterNode.test.ts]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { numberToHexUnpadded } from "@noble/curves/utils.js";
import { useCallback, useMemo } from "react";

export type FilterState = {
  nodeName: string;
  hopsAway: [number, number];
  lastHeard: [number, number];
  isFavorite: boolean | undefined;
  viaMqtt: boolean | undefined;
  snr: [number, number];
  channelUtilization: [number, number];
  airUtilTx: [number, number];
  batteryLevel: [number, number];
  voltage: [number, number];
  role: Protobuf.Config.Config_DeviceConfig_Role[];
  hwModel: Protobuf.Mesh.HardwareModel[];
  showUnheard: boolean | undefined;
  hopsUnknown: boolean | undefined;
};
...
```