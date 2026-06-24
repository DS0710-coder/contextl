# RadioConfig.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/domain/RadioConfig.ts`
- **Extension:** `.ts`
- **Size:** 571 bytes
- **Centrality Score:** 0.0027
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RadioConfigSection`
- `RadioConfig`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]
- [[packages/sdk/src/features/config/infrastructure/ConfigMapper.ts.md|packages/sdk/src/features/config/infrastructure/ConfigMapper.ts]]
- [[packages/sdk/src/features/config/state/configStore.ts.md|packages/sdk/src/features/config/state/configStore.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

/**
 * The radio-config sections keyed by their protobuf variant case (excluding
 * the "no variant" undefined case).
 */
export type RadioConfigSection = Exclude<
  Protobuf.Config.Config["payloadVariant"]["case"],
  undefined
>;

/**
 * Section -> proto-payload map, derived directly from the Config message so
 * new variants stay typed automatically.
 */
export type RadioConfig = {
  readonly [V in RadioConfigSection]?: Extract<
    Protobuf.Config.Config["payloadVariant"],
    { case: V }
  >["value"];
...
```