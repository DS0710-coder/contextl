# MeshError.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/core/errors/MeshError.ts`
- **Extension:** `.ts`
- **Size:** 1011 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
Typed error hierarchy mirroring `@meshtastic/sdk` (PR #1050). New application
use-cases return `Result<T, MeshError>` instead of throwing; transport-level
failures are represented as concrete subclasses so callers can branch on
`instanceof` rather than string-matching messages.

## Structural Outline
- `MeshError`
- `ConfigCommitError`
- `toMeshError`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts.md|apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
/**
 * Typed error hierarchy mirroring `@meshtastic/sdk` (PR #1050). New application
 * use-cases return `Result<T, MeshError>` instead of throwing; transport-level
 * failures are represented as concrete subclasses so callers can branch on
 * `instanceof` rather than string-matching messages.
 */
export class MeshError extends Error {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = "MeshError";
  }
}

export class ConfigCommitError extends MeshError {
  constructor(section: string, options?: ErrorOptions) {
    super(`Failed to commit config section "${section}"`, options);
    this.name = "ConfigCommitError";
  }
}

...
```