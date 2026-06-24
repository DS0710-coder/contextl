# Xmodem.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/xmodem/Xmodem.ts`
- **Extension:** `.ts`
- **Size:** 3663 bytes
- **Centrality Score:** 0.0049
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `XmodemProps`
- `Xmodem`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]
- [[packages/sdk/src/shim/legacyUtils.ts.md|packages/sdk/src/shim/legacyUtils.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import crc16ccitt from "crc/calculators/crc16ccitt";

type XmodemProps = (toRadio: Uint8Array, id?: number) => Promise<number>;

export class Xmodem {
  private sendRaw: XmodemProps;
  private rxBuffer: Uint8Array[];
  private txBuffer: Uint8Array[];
  private textEncoder: TextEncoder;
  private counter: number;

  constructor(sendRaw: XmodemProps) {
    this.sendRaw = sendRaw;
    this.rxBuffer = [];
    this.txBuffer = [];
    this.textEncoder = new TextEncoder();
    this.counter = 0;
  }
...
```