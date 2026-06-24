# deviceStore.mock.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/deviceStore/deviceStore.mock.ts`
- **Extension:** `.ts`
- **Size:** 2107 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/sdk";
import { vi } from "vitest";
import type { Device } from "./index.ts";

/**
 * You can spread this base mock in your tests and override only the
 * properties relevant to a specific test case.
 *
 * @example
 * vi.mocked(useDevice).mockReturnValue({
 * ...mockDeviceStore,
 * getNode: (nodeNum) => mockNodes.get(nodeNum),
 * });
 */
export const mockDeviceStore: Device = {
  id: 0,
  myNodeNum: 123456,
  status: 5 as const,
  connectionPhase: "disconnected",
  connectionId: null,
...
```