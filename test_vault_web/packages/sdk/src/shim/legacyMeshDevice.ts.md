# legacyMeshDevice.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/shim/legacyMeshDevice.ts`
- **Extension:** `.ts`
- **Size:** 10816 bytes
- **Centrality Score:** 0.0033
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
Coarse facade providing the legacy `MeshDevice` surface — preserved
after Phase C because the web app's `connection.factoryResetDevice()` /
`connection.reboot()` / etc. callsites still depend on it. Delegates to
the new `MeshClient` + feature slices. New consumers should reach into
the slice clients (`client.config`, `client.chat`, …) directly.

## Structural Outline
- `MeshClientOptions`
- `Destination`
- `PacketMetadata`
- `MeshDeviceOptions`
- `MeshDevice`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/core/xmodem/Xmodem.ts.md|packages/sdk/src/core/xmodem/Xmodem.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Source Code Snippet
```ts
/**
 * Coarse facade providing the legacy `MeshDevice` surface — preserved
 * after Phase C because the web app's `connection.factoryResetDevice()` /
 * `connection.reboot()` / etc. callsites still depend on it. Delegates to
 * the new `MeshClient` + feature slices. New consumers should reach into
 * the slice clients (`client.config`, `client.chat`, …) directly.
 */

import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { Logger } from "tslog";
import {
  MeshClient,
  type MeshClientOptions,
} from "../core/client/MeshClient.ts";
import type { EventBus } from "../core/event-bus/EventBus.ts";
import type { Queue } from "../core/queue/Queue.ts";
import type { Transport } from "../core/transport/Transport.ts";
import { DeviceStatusEnum } from "../core/transport/Transport.ts";
import {
...
```