# color.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/color.ts`
- **Extension:** `.ts`
- **Size:** 710 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RGBColor`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/core/utils/color.test.ts.md|apps/web/src/core/utils/color.test.ts]]

## Source Code Snippet
```ts
export interface RGBColor {
  r: number;
  g: number;
  b: number;
}

export const hexToRgb = (hex: number): RGBColor => ({
  r: (hex & 0xff0000) >> 16,
  g: (hex & 0x00ff00) >> 8,
  b: hex & 0x0000ff,
});

export const rgbToHex = (c: RGBColor): number =>
  (Math.round(c.r) << 16) | (Math.round(c.g) << 8) | Math.round(c.b);

export const isLightColor = (c: RGBColor): boolean =>
  (c.r * 299 + c.g * 587 + c.b * 114) / 1000 > 127.5;

export const getColorFromNodeNum = (nodeNum: number): RGBColor => {
  // Extract RGB values directly from nodeNum (treated as hex color)
...
```