# PacketId.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/identifiers/PacketId.ts`
- **Extension:** `.ts`
- **Size:** 221 bytes
- **Centrality Score:** 0.0048
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `generatePacketId`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/application/SendWaypointUseCase.ts.md|packages/sdk/src/features/chat/application/SendWaypointUseCase.ts]]
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]

## Source Code Snippet
```ts
export function generatePacketId(): number {
  const seed = crypto.getRandomValues(new Uint32Array(1));
  if (!seed[0]) {
    throw new Error("Cannot generate CSPRN");
  }
  return Math.floor(seed[0] * 2 ** -32 * 1e9);
}
```