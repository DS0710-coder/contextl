# ModuleConfig.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts`
- **Extension:** `.ts`
- **Size:** 726 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ModuleConfigSection`
- `ModuleConfig`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]
- [[apps/web/src/sdk-preview/features/config/index.ts.md|apps/web/src/sdk-preview/features/config/index.ts]]
- [[apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts.md|apps/web/src/sdk-preview/features/config/infrastructure/ConfigMapper.ts]]
- [[apps/web/src/sdk-preview/features/config/infrastructure/configBuilders.ts.md|apps/web/src/sdk-preview/features/config/infrastructure/configBuilders.ts]]

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/core";

/**
 * The module-config sections keyed by their protobuf variant case. Because this
 * is derived from the firmware-current protobufs, the new modules synced in
 * this branch — `trafficManagement`, `statusmessage`, `tak`, `remoteHardware` —
 * are already members with zero extra code.
 */
export type ModuleConfigSection = Exclude<
  Protobuf.ModuleConfig.ModuleConfig["payloadVariant"]["case"],
  undefined
>;

/** Section -> proto-payload map, derived directly from the `ModuleConfig` message. */
export type ModuleConfig = {
  readonly [V in ModuleConfigSection]?: Extract<
    Protobuf.ModuleConfig.ModuleConfig["payloadVariant"],
    { case: V }
  >["value"];
};
```