# SqlocalNodesRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 2520 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `node`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { Node } from "@meshtastic/sdk";
import { beforeEach, describe, expect, it } from "vitest";
import type { SqlocalDb } from "../db.ts";
import { createMemoryDb } from "../testing/createMemoryDb.ts";
import { SqlocalNodesRepository } from "./SqlocalNodesRepository.ts";

function node(num: number, partial: Partial<Node> = {}): Node {
  return {
    num,
    isFavorite: false,
    isIgnored: false,
    user: undefined,
    position: undefined,
    deviceMetrics: undefined,
    lastHeard: undefined,
    snr: undefined,
    ...partial,
  };
...
```