# lora.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/lora.test.ts`
- **Extension:** `.ts`
- **Size:** 350 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { describe, expect, it } from "vitest";

describe("LoRa modem presets", () => {
  it("includes LONG_TURBO modem preset", () => {
    expect(
      Object.prototype.hasOwnProperty.call(
        Protobuf.Config.Config_LoRaConfig_ModemPreset,
        "LONG_TURBO",
      ),
    ).toBe(true);
  });
});
```