# useBrowserFeatureDetection.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useBrowserFeatureDetection.ts`
- **Extension:** `.ts`
- **Size:** 898 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BrowserFeature`
- `BrowserSupport`
- `useBrowserFeatureDetection`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]

## Source Code Snippet
```ts
import { useMemo } from "react";

export type BrowserFeature = "Web Bluetooth" | "Web Serial" | "Secure Context";

interface BrowserSupport {
  supported: BrowserFeature[];
  unsupported: BrowserFeature[];
}

export function useBrowserFeatureDetection(): BrowserSupport {
  const support = useMemo(() => {
    const features: [BrowserFeature, boolean][] = [
      ["Web Bluetooth", !!navigator.bluetooth],
      ["Web Serial", !!navigator.serial],
      [
        "Secure Context",
        globalThis.location.protocol === "https:" ||
          globalThis.location.hostname === "localhost",
      ],
    ];
...
```