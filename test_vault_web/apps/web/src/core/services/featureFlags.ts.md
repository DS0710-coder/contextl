# featureFlags.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/services/featureFlags.ts`
- **Extension:** `.ts`
- **Size:** 2171 bytes
- **Centrality Score:** 0.0029
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FlagKey`
- `Flags`
- `Listener`
- `FeatureFlags`
- `createFeatureFlags`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/hooks/useFeatureFlags.ts.md|apps/web/src/core/hooks/useFeatureFlags.ts]]
- [[apps/web/src/core/services/dev-overrides.ts.md|apps/web/src/core/services/dev-overrides.ts]]
- [[apps/web/src/core/stores/appStore/index.ts.md|apps/web/src/core/stores/appStore/index.ts]]

## Source Code Snippet
```ts
import { z } from "zod";

/** Map feature keys -> env var names (Vite exposes only VITE_*). */
export const FLAG_ENV = {
  persistMessages: "VITE_PERSIST_MESSAGES",
  persistDevices: "VITE_PERSIST_DEVICES",
  persistApp: "VITE_PERSIST_APP",
} as const;

export type FlagKey = keyof typeof FLAG_ENV;
export type Flags = Record<FlagKey, boolean>;

type Listener = () => void;

const present = z
  .string()
  .optional()
  .transform((v) => v !== undefined);

const mutableShape: Record<string, z.ZodTypeAny> = {};
...
```