# ModuleConfig.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/domain/ModuleConfig.ts`
- **Extension:** `.ts`
- **Size:** 349 bytes
- **Centrality Score:** 0.0027
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ModuleConfigSection`
- `ModuleConfig`

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

export type ModuleConfigSection = Exclude<
  Protobuf.ModuleConfig.ModuleConfig["payloadVariant"]["case"],
  undefined
>;

export type ModuleConfig = {
  readonly [V in ModuleConfigSection]?: Extract<
    Protobuf.ModuleConfig.ModuleConfig["payloadVariant"],
    { case: V }
  >["value"];
};
```