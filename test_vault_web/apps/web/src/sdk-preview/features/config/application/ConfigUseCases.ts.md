# ConfigUseCases.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/application/ConfigUseCases.ts`
- **Extension:** `.ts`
- **Size:** 1604 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/client/MeshClientPort.ts.md|apps/web/src/sdk-preview/core/client/MeshClientPort.ts]]
- [[apps/web/src/sdk-preview/core/errors/MeshError.ts.md|apps/web/src/sdk-preview/core/errors/MeshError.ts]]

## Imported By (Dependents)
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/core";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClientPort } from "../../../core/client/MeshClientPort.ts";
import { type MeshError, toMeshError } from "../../../core/errors/MeshError.ts";

/**
 * Application use-cases for the config slice. Each wraps a transport call in a
 * `Result<number, MeshError>` instead of throwing — mirroring the SDK's
 * use-case layer from PR #1050. The returned number is the sent packet id.
 */

export async function beginEditSettings(
  client: MeshClientPort,
): Promise<ResultType<number, MeshError>> {
  try {
    return Result.ok(await client.beginEditSettings());
  } catch (error) {
    return Result.err(toMeshError(error));
  }
...
```