# useFilterNode.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Filter/useFilterNode.test.ts`
- **Extension:** `.ts`
- **Size:** 7933 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `createMockNode`

## Imports (Dependencies)
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { useFilterNode } from "@components/generic/Filter/useFilterNode.ts";
import { Protobuf } from "@meshtastic/sdk";
import { renderHook } from "@testing-library/react";
import { describe, expect, it } from "vitest";

function createMockNode(): Protobuf.Mesh.NodeInfo {
  return {
    $typeName: "meshtastic.NodeInfo",
    num: 1234567890,
    snr: -10.2,
    lastHeard: 1747519674,
    channel: 0,
    viaMqtt: false,
    isFavorite: true,
    isIgnored: false,
    isMuted: false,
    hopsAway: 2,
    isKeyManuallyVerified: false,
    user: {
      $typeName: "meshtastic.User",
...
```