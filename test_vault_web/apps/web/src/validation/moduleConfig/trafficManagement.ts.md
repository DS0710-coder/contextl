# trafficManagement.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/trafficManagement.ts`
- **Extension:** `.ts`
- **Size:** 829 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TrafficManagementValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const TrafficManagementValidationSchema = z.object({
  enabled: z.boolean(),
  positionDedupEnabled: z.boolean(),
  positionPrecisionBits: z.coerce.number().int().min(0).max(32),
  positionMinIntervalSecs: z.coerce.number().int().min(0),
  nodeinfoDirectResponse: z.boolean(),
  nodeinfoDirectResponseMaxHops: z.coerce.number().int().min(0).max(7),
  rateLimitEnabled: z.boolean(),
  rateLimitWindowSecs: z.coerce.number().int().min(0),
  rateLimitMaxPackets: z.coerce.number().int().min(0),
  dropUnknownEnabled: z.boolean(),
  unknownPacketThreshold: z.coerce.number().int().min(0),
  exhaustHopTelemetry: z.boolean(),
  exhaustHopPosition: z.boolean(),
  routerPreserveHops: z.boolean(),
});

export type TrafficManagementValidation = z.infer<
...
```