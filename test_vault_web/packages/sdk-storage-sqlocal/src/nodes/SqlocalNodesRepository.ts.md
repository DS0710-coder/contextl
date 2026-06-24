# SqlocalNodesRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts`
- **Extension:** `.ts`
- **Size:** 4205 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SqlocalNodesRepositoryOptions`
- `SqlocalNodesRepository`
- `NodeRow`
- `rowToNode`
- `nodeToRow`
- `base64Encode`
- `base64Decode`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/nodes.ts.md|packages/sdk-storage-sqlocal/src/schema/nodes.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/index.ts.md|packages/sdk-storage-sqlocal/src/nodes/index.ts]]

## Source Code Snippet
```ts
import type { Node, NodesRepository } from "@meshtastic/sdk";
import { fromBinary, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { and, eq } from "drizzle-orm";
import type { SqlocalDb } from "../db.ts";
import { nodes } from "../schema/nodes.ts";

export interface SqlocalNodesRepositoryOptions {
  deviceId: number;
}

/**
 * Persists the snapshot of the device's NodeDB. user/position/metrics are
 * stored as base64-encoded protobuf bytes — round-trip safe across schema
 * additions because the wire shape is the source of truth.
 */
export class SqlocalNodesRepository implements NodesRepository {
  private readonly db: SqlocalDb;
  private readonly deviceId: number;

...
```