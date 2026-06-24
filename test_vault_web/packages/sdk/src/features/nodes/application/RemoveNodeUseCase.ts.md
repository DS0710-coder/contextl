# RemoveNodeUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts`
- **Extension:** `.ts`
- **Size:** 926 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]

## Source Code Snippet
```ts
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { sendAdminMessage } from "../../device/infrastructure/AdminMessageSender.ts";

export async function removeNodeByNum(
  client: MeshClient,
  nodeNum: number,
): Promise<ResultType<number, Error>> {
  try {
    const id = await sendAdminMessage(client, {
      case: "removeByNodenum",
      value: nodeNum,
    });
    return Result.ok(id);
  } catch (e) {
    return Result.err(e instanceof Error ? e : new Error(String(e)));
  }
}

...
```