# MultiTabCoordinator.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.ts`
- **Extension:** `.ts`
- **Size:** 2460 bytes
- **Centrality Score:** 0.0031
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
Coordination across browser tabs of the same origin.

- **Web Locks API** (`navigator.locks`): a single tab holds the writer lock
for a given resource; others queue. Used to serialize destructive
operations (full DB rebuilds, bulk imports) when needed.
- **BroadcastChannel**: lock-free pub/sub for "data changed" notifications,
so reader tabs can refresh their views without polling.

sqlocal handles low-level DB write serialization via OPFS file locks; this
layer is for app-level changes ("messages-changed for device 5, channel 0")
so the chat slice in another tab can re-query after a write.

## Structural Outline
- `ChangeKind`
- `ChangeEvent`
- `MultiTabCoordinator`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.broadcast.test.ts.md|packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.broadcast.test.ts]]
- [[packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.test.ts.md|packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.test.ts]]
- [[packages/sdk-storage-sqlocal/src/coordination/index.ts.md|packages/sdk-storage-sqlocal/src/coordination/index.ts]]

## Source Code Snippet
```ts
/**
 * Coordination across browser tabs of the same origin.
 *
 * - **Web Locks API** (`navigator.locks`): a single tab holds the writer lock
 *   for a given resource; others queue. Used to serialize destructive
 *   operations (full DB rebuilds, bulk imports) when needed.
 * - **BroadcastChannel**: lock-free pub/sub for "data changed" notifications,
 *   so reader tabs can refresh their views without polling.
 *
 * sqlocal handles low-level DB write serialization via OPFS file locks; this
 * layer is for app-level changes ("messages-changed for device 5, channel 0")
 * so the chat slice in another tab can re-query after a write.
 */

export type ChangeKind =
  | "messages-changed"
  | "nodes-changed"
  | "telemetry-changed";

export interface ChangeEvent {
...
```