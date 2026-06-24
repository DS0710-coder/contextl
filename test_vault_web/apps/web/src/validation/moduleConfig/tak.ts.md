# tak.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/tak.ts`
- **Extension:** `.ts`
- **Size:** 335 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TakValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/core";
import { z } from "zod/v4";

const TeamEnum = z.enum(Protobuf.ATAK.Team);
const MemberRoleEnum = z.enum(Protobuf.ATAK.MemberRole);

export const TakValidationSchema = z.object({
  team: TeamEnum,
  role: MemberRoleEnum,
});

export type TakValidation = z.infer<typeof TakValidationSchema>;
```