# useConfig.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useConfig.ts`
- **Extension:** `.ts`
- **Size:** 805 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useConfig`
- `useModuleConfig`
- `useIsRegionUnset`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ModuleConfig, RadioConfig } from "@meshtastic/sdk";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export function useConfig(): RadioConfig {
  const client = useClient();
  return useSignal(client.config.radio);
}

export function useModuleConfig(): ModuleConfig {
  const client = useClient();
  return useSignal(client.config.modules);
}

/**
 * `true` when the connected device's LoRa region is UNSET — the canonical
 * "this device was just flashed and hasn't been provisioned" cue. See
 * `ConfigClient.isRegionUnset` for semantics + reference to the equivalent
 * Meshtastic-Android flow.
 */
...
```