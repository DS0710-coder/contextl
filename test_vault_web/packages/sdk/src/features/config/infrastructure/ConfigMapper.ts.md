# ConfigMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/infrastructure/ConfigMapper.ts`
- **Extension:** `.ts`
- **Size:** 723 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/config/domain/ModuleConfig.ts.md|packages/sdk/src/features/config/domain/ModuleConfig.ts]]
- [[packages/sdk/src/features/config/domain/RadioConfig.ts.md|packages/sdk/src/features/config/domain/RadioConfig.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { ModuleConfig } from "../domain/ModuleConfig.ts";
import type { RadioConfig } from "../domain/RadioConfig.ts";

export const ConfigMapper = {
  mergeRadio(
    existing: RadioConfig,
    incoming: Protobuf.Config.Config,
  ): RadioConfig {
    const variant = incoming.payloadVariant;
    if (!variant.case) return existing;
    return { ...existing, [variant.case]: variant.value };
  },
  mergeModule(
    existing: ModuleConfig,
    incoming: Protobuf.ModuleConfig.ModuleConfig,
  ): ModuleConfig {
    const variant = incoming.payloadVariant;
    if (!variant.case) return existing;
    return { ...existing, [variant.case]: variant.value };
...
```