# usePositionFlags.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/usePositionFlags.ts`
- **Extension:** `.ts`
- **Size:** 4279 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FlagName`
- `UsePositionFlagsProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Form/FormMultiSelect.tsx.md|apps/web/src/components/Form/FormMultiSelect.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]

## Source Code Snippet
```ts
import { useCallback, useMemo, useState } from "react";

export const FLAGS_CONFIG = {
  UNSET: { value: 0, i18nKey: "position.flags.unset" },
  ALTITUDE: { value: 1, i18nKey: "position.flags.altitude" },
  ALTITUDE_MSL: { value: 2, i18nKey: "position.flags.altitudeMsl" },
  ALTITUDE_GEOIDAL_SEPARATION: {
    value: 4,
    i18nKey: "position.flags.altitudeGeoidalSeparation",
  },
  DOP: {
    value: 8,
    i18nKey: "position.flags.dop",
  },
  HDOP_VDOP: {
    value: 16,
    i18nKey: "position.flags.hdopVdop",
  },
  NUM_SATELLITES: {
    value: 32,
...
```