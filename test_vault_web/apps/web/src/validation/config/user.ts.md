# user.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/user.ts`
- **Extension:** `.ts`
- **Size:** 642 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UserValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/User.tsx.md|apps/web/src/components/PageComponents/Settings/User.tsx]]

## Source Code Snippet
```ts
import { t } from "i18next";
import { z } from "zod/v4";

export const UserValidationSchema = z.object({
  // Read-only display fields (preserved on submit).
  nodeId: z.string().optional(),
  hardwareModel: z.string().optional(),
  longName: z
    .string()
    .min(1, t("user.longName.validation.min"))
    .max(40, t("user.longName.validation.max")),
  shortName: z
    .string()
    .min(1, t("user.shortName.validation.min"))
    .max(4, t("user.shortName.validation.max")),
  isUnmessageable: z.boolean().default(false),
  isLicensed: z.boolean().default(false),
});

export type UserValidation = z.infer<typeof UserValidationSchema>;
```