# configBuilders.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/infrastructure/configBuilders.ts`
- **Extension:** `.ts`
- **Size:** 1078 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `buildRadioConfig`
- `buildModuleConfig`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/ModuleConfig.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts.md|apps/web/src/sdk-preview/features/config/domain/RadioConfig.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import { Protobuf } from "@meshtastic/core";
import type {
  ModuleConfig,
  ModuleConfigSection,
} from "../domain/ModuleConfig.ts";
import type { RadioConfig, RadioConfigSection } from "../domain/RadioConfig.ts";

/** Wrap a single radio-config section value back into a `Config` message. */
export function buildRadioConfig<K extends RadioConfigSection>(
  section: K,
  value: NonNullable<RadioConfig[K]>,
): Protobuf.Config.Config {
  return create(Protobuf.Config.ConfigSchema, {
    payloadVariant: {
      case: section,
      value,
    } as Protobuf.Config.Config["payloadVariant"],
  });
}
...
```