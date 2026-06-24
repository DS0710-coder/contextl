# createZodResolver.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/createZodResolver.ts`
- **Extension:** `.ts`
- **Size:** 1530 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createZodResolver`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]

## Source Code Snippet
```ts
import type {
  FieldError,
  FieldErrors,
  FieldValues,
  Resolver,
  ResolverOptions,
  ResolverResult,
} from "react-hook-form";
import type { ZodType } from "zod/v4";

export function createZodResolver<T extends FieldValues>(
  schema: ZodType<T, unknown>,
): Resolver<T, unknown> {
  return (
    values: T,
    _context: unknown,
    _options?: ResolverOptions<T>,
  ): ResolverResult<T> => {
    const result = schema.safeParse(values);
    if (result.success) {
...
```