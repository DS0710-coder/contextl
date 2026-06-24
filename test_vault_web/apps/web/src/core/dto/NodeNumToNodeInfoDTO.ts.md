# NodeNumToNodeInfoDTO.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/dto/NodeNumToNodeInfoDTO.ts`
- **Extension:** `.ts`
- **Size:** 995 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createDefaultUser`
- `ensureDefaultUser`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import { Protobuf } from "@meshtastic/sdk";

function createDefaultUser(num: number): Protobuf.Mesh.User {
  const userIdHex = num.toString(16).toUpperCase().padStart(2, "0");
  const userId = `!${userIdHex}`;
  const last4 = userIdHex.slice(-4);
  const longName = `Meshtastic ${last4}`;
  const shortName = last4;

  return create(Protobuf.Mesh.UserSchema, {
    id: userId,
    longName: longName.toString(),
    shortName: shortName.toString(),
  });
}

export function ensureDefaultUser(
  node: Protobuf.Mesh.NodeInfo,
): Protobuf.Mesh.NodeInfo {
...
```