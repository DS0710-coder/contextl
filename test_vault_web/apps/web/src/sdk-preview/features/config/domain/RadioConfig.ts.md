# RadioConfig.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts`
- **Extension:** `.ts`
- **Size:** 648 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RadioConfigSection`
- `RadioConfig`

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
 * The radio-config sections keyed by their protobuf variant case (excluding the
 * "no variant" undefined case). Derived directly from the `Config` message, so
 * new firmware variants stay typed automatically — no per-section maintenance.
 */
export type RadioConfigSection = Exclude<
  Protobuf.Config.Config["payloadVariant"]["case"],
  undefined
>;

/** Section -> proto-payload map, derived directly from the `Config` message. */
export type RadioConfig = {
  readonly [V in RadioConfigSection]?: Extract<
    Protobuf.Config.Config["payloadVariant"],
    { case: V }
  >["value"];
};
```