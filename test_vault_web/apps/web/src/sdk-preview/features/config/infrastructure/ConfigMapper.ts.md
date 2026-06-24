# ConfigMapper.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts`
- **Extension:** `.ts`
- **Size:** 985 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/core";
import type { ModuleConfig } from "../domain/ModuleConfig.ts";
import type { RadioConfig } from "../domain/RadioConfig.ts";

/**
 * Translates inbound protobuf `Config` / `ModuleConfig` packets into the slice's
 * section-keyed domain shape. Fully generic — new firmware sections flow through
 * with no code change, exactly like the SDK mapper in PR #1050.
 */
export const ConfigMapper = {
  mergeRadio(
    existing: RadioConfig,
    incoming: Protobuf.Config.Config,
  ): RadioConfig {
    const variant = incoming.payloadVariant;
    if (!variant.case) {
      return existing;
    }
    return { ...existing, [variant.case]: variant.value };
  },
...
```