# validation.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/AddConnectionDialog/validation.ts`
- **Extension:** `.ts`
- **Size:** 1405 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]

## Source Code Snippet
```ts
import z from "zod";

export const urlOrIpv4Schema = z
  .string()
  .trim()
  .refine((val) => {
    const input = val.replace(/^https?:\/\//i, "");

    // Split input into host and port (port is optional)
    const lastColonIndex = input.lastIndexOf(":");
    let host = input;
    let port = null;

    if (lastColonIndex !== -1) {
      const potentialPort = input.substring(lastColonIndex + 1);
      if (/^\d+$/.test(potentialPort)) {
        host = input.substring(0, lastColonIndex);
        port = parseInt(potentialPort, 10);
      }
    }
...
```