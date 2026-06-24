# remoteHardware.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/remoteHardware.ts`
- **Extension:** `.ts`
- **Size:** 426 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RemoteHardwareValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const RemoteHardwareValidationSchema = z.object({
  enabled: z.boolean(),
  allowUndefinedPinAccess: z.boolean(),
  // Preserved untouched: the form does not yet edit the available-pins list,
  // so round-trip it to avoid clearing pins configured elsewhere.
  availablePins: z.array(z.any()),
});

export type RemoteHardwareValidation = z.infer<
  typeof RemoteHardwareValidationSchema
>;
```