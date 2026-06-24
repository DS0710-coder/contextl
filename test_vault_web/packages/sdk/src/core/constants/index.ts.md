# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/constants/index.ts`
- **Extension:** `.ts`
- **Size:** 124 bytes
- **Centrality Score:** 0.0045
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]

## Source Code Snippet
```ts
const broadcastNum = 0xffffffff;

const minFwVer = 2.2;

export const Constants = {
  broadcastNum,
  minFwVer,
} as const;
```