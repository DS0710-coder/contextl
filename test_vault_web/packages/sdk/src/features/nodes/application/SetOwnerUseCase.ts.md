# SetOwnerUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts`
- **Extension:** `.ts`
- **Size:** 651 bytes
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
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { sendAdminMessage } from "../../device/infrastructure/AdminMessageSender.ts";

export async function setOwner(
  client: MeshClient,
  owner: Protobuf.Mesh.User,
): Promise<ResultType<number, Error>> {
  try {
    const id = await sendAdminMessage(client, {
      case: "setOwner",
      value: owner,
    });
    return Result.ok(id);
  } catch (e) {
    return Result.err(e instanceof Error ? e : new Error(String(e)));
  }
}
```