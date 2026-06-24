# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-deno/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 1126 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TransportDeno`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-deno/mod.ts.md|packages/transport-deno/mod.ts]]

## Source Code Snippet
```ts
import type { DeviceOutput, Transport } from "@meshtastic/sdk";
import { fromDeviceStream, toDeviceStream } from "@meshtastic/sdk";

export class TransportDeno implements Transport {
  private _toDevice: WritableStream<Uint8Array>;
  private _fromDevice: ReadableStream<DeviceOutput>;
  private connection: Deno.Conn | undefined;

  public static async create(hostname: string): Promise<TransportDeno> {
    const connection = await Deno.connect({
      hostname,
      port: 4403,
    });
    return new TransportDeno(connection);
  }

  constructor(connection: Deno.Conn) {
    this.connection = connection;
    const toStream = toDeviceStream();
    toStream.readable.pipeTo(this.connection.writable);
...
```