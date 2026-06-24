# createFakeTransport.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/testing/createFakeTransport.ts`
- **Extension:** `.ts`
- **Size:** 3972 bytes
- **Centrality Score:** 0.0047
- **In-Degree (Imported By):** 16
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FakeTransportHandle`
- `MyNodeInfoInit`
- `NodeInfoInit`
- `FakeResponder`
- `createFakeTransport`
- `enqueueFromRadio`

## Imports (Dependencies)
- [[packages/sdk/src/core/packet-codec/fromDevice.ts.md|packages/sdk/src/core/packet-codec/fromDevice.ts]]
- [[packages/sdk/src/core/packet-codec/toDevice.ts.md|packages/sdk/src/core/packet-codec/toDevice.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/core/client/MeshClient.progress.test.ts.md|packages/sdk/src/core/client/MeshClient.progress.test.ts]]
- [[packages/sdk/src/core/registry/MeshRegistry.test.ts.md|packages/sdk/src/core/registry/MeshRegistry.test.ts]]
- [[packages/sdk/src/core/testing/index.ts.md|packages/sdk/src/core/testing/index.ts]]
- [[packages/sdk/src/features/channels/ChannelsClient.test.ts.md|packages/sdk/src/features/channels/ChannelsClient.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.drafts.test.ts.md|packages/sdk/src/features/chat/ChatClient.drafts.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.persistence.test.ts.md|packages/sdk/src/features/chat/ChatClient.persistence.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.send.test.ts.md|packages/sdk/src/features/chat/ChatClient.send.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.unread.test.ts.md|packages/sdk/src/features/chat/ChatClient.unread.test.ts]]
- [[packages/sdk/src/features/config/ConfigClient.test.ts.md|packages/sdk/src/features/config/ConfigClient.test.ts]]
- [[packages/sdk/src/features/config/ConfigEditor.test.ts.md|packages/sdk/src/features/config/ConfigEditor.test.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.errors.test.ts.md|packages/sdk/src/features/nodes/NodesClient.errors.test.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.test.ts.md|packages/sdk/src/features/nodes/NodesClient.test.ts]]
- [[packages/sdk/src/features/position/PositionClient.test.ts.md|packages/sdk/src/features/position/PositionClient.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.test.ts]]
- [[packages/sdk/tests/integration/fake-transport.test.ts.md|packages/sdk/tests/integration/fake-transport.test.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { toDeviceStream } from "../packet-codec/toDevice.ts";
import { fromDeviceStream } from "../packet-codec/fromDevice.ts";
import type { Transport } from "../transport/Transport.ts";

export interface FakeTransportHandle {
  transport: Transport;
  respond: FakeResponder;
  /** Exposes what the client has written to the device (already unframed). */
  sent: Uint8Array[];
  /** Closes the simulated connection. */
  close(): Promise<void>;
}

type MyNodeInfoInit = Parameters<
  typeof create<typeof Protobuf.Mesh.MyNodeInfoSchema>
>[1];
type NodeInfoInit = Parameters<
  typeof create<typeof Protobuf.Mesh.NodeInfoSchema>
...
```