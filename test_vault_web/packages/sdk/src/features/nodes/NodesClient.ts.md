# NodesClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/NodesClient.ts`
- **Extension:** `.ts`
- **Size:** 8468 bytes
- **Centrality Score:** 0.0021
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodesClientOptions`
- `NodesClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/FavoriteNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/IgnoreNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts.md|packages/sdk/src/features/nodes/application/RemoveNodeUseCase.ts]]
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]
- [[packages/sdk/src/features/nodes/domain/NodeError.ts.md|packages/sdk/src/features/nodes/domain/NodeError.ts]]
- [[packages/sdk/src/features/nodes/domain/NodesRepository.ts.md|packages/sdk/src/features/nodes/domain/NodesRepository.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts.md|packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts.md|packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts.md|packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts]]
- [[packages/sdk/src/features/nodes/state/nodeErrorsStore.ts.md|packages/sdk/src/features/nodes/state/nodeErrorsStore.ts]]
- [[packages/sdk/src/features/nodes/state/nodesStore.ts.md|packages/sdk/src/features/nodes/state/nodesStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import type { Node } from "./domain/Node.ts";
import type { NodeError, NodeErrorType } from "./domain/NodeError.ts";
import type { NodesRepository } from "./domain/NodesRepository.ts";
import { NodeMapper } from "./infrastructure/NodeMapper.ts";
import { InMemoryNodesRepository } from "./infrastructure/repositories/InMemoryNodesRepository.ts";
import { validateIncomingNode } from "./infrastructure/nodeValidation.ts";
import { NodeErrorsStore } from "./state/nodeErrorsStore.ts";
import { NodesStore } from "./state/nodesStore.ts";
import {
  favoriteNode,
  removeFavoriteNode,
} from "./application/FavoriteNodeUseCase.ts";
import {
  ignoreNode,
  removeIgnoredNode,
...
```