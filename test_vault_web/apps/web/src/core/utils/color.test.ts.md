# color.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/color.test.ts`
- **Extension:** `.ts`
- **Size:** 2993 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RGBColor`

## Imports (Dependencies)
- [[apps/web/src/core/utils/color.ts.md|apps/web/src/core/utils/color.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import {
  getColorFromNodeNum,
  hexToRgb,
  isLightColor,
  type RGBColor,
  rgbToHex,
} from "./color.ts";

describe("hexToRgb", () => {
  it.each([
    [0x000000, { r: 0, g: 0, b: 0 }],
    [0xffffff, { r: 255, g: 255, b: 255 }],
    [0x123456, { r: 0x12, g: 0x34, b: 0x56 }],
    [0xff8000, { r: 255, g: 128, b: 0 }],
  ])("parses 0x%s correctly", (hex, expected) => {
    expect(hexToRgb(hex)).toEqual(expected);
  });
});

...
```