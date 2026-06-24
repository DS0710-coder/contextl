# RegionSetupReminder.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/RegionSetupReminder.tsx`
- **Extension:** `.tsx`
- **Size:** 2097 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { useToast } from "@core/hooks/useToast.ts";
import { useIsRegionUnset } from "@meshtastic/sdk-react";
import { useNavigate } from "@tanstack/react-router";
import { useEffect, useRef } from "react";
import { useTranslation } from "react-i18next";

/**
 * Mirrors Meshtastic-Android's `regionUnset` cue. A freshly-flashed device
 * has `Config.LoRa.region == UNSET` until the user picks one, and won't
 * transmit at all in that state. We surface a non-dismissable toast that
 * deep-links into the LoRa settings tab so first-time users land in the
 * right place without hunting through the menu.
 *
 * The toast appears as soon as the SDK reports `isRegionUnset == true`
 * (after the LoRa config packet arrives) and dismisses itself the moment
 * a real region is committed.
 */
export const RegionSetupReminder = (): null => {
  const isRegionUnset = useIsRegionUnset();
...
```