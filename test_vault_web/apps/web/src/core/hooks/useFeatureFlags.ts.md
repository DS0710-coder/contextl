# useFeatureFlags.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useFeatureFlags.ts`
- **Extension:** `.ts`
- **Size:** 523 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FlagKey`
- `Flags`
- `useFeatureFlags`
- `useFeatureFlag`

## Imports (Dependencies)
- [[apps/web/src/core/services/featureFlags.ts.md|apps/web/src/core/services/featureFlags.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import {
  type FlagKey,
  type Flags,
  featureFlags,
} from "@core/services/featureFlags.ts";
import * as React from "react";

export function useFeatureFlags(): Flags {
  return React.useSyncExternalStore(
    (cb) => featureFlags.subscribe(cb),
    () => featureFlags.all(),
    () => featureFlags.all(),
  );
}

export function useFeatureFlag(key: FlagKey): boolean {
  return React.useSyncExternalStore(
    (cb) => featureFlags.subscribe(cb),
    () => featureFlags.get(key),
    () => featureFlags.get(key),
...
```