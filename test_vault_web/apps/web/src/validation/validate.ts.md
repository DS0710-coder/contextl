# validate.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/validate.ts`
- **Extension:** `.ts`
- **Size:** 383 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `validateSchema`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { ZodError, ZodType } from "zod/v4";

export function validateSchema<T>(
  schema: ZodType<T>,
  data: unknown,
): { success: true; data: T } | { success: false; errors: ZodError["issues"] } {
  const result = schema.safeParse(data);
  if (result.success) {
    return { success: true, data: result.data };
  }
  return { success: false, errors: result.error.issues };
}
```