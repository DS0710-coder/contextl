# toDevice.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/packet-codec/toDevice.ts`
- **Extension:** `.ts`
- **Size:** 530 bytes
- **Centrality Score:** 0.0049
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
Pads outbound packets with the 0x94 0xC3 framing header and length prefix.

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/packet-codec/index.ts.md|packages/sdk/src/core/packet-codec/index.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/shim/legacyUtils.ts.md|packages/sdk/src/shim/legacyUtils.ts]]

## Source Code Snippet
```ts
/**
 * Pads outbound packets with the 0x94 0xC3 framing header and length prefix.
 */
export const toDeviceStream: () => TransformStream<
  Uint8Array,
  Uint8Array
> = () => {
  return new TransformStream<Uint8Array, Uint8Array>({
    transform(chunk: Uint8Array, controller): void {
      const bufLen = chunk.length;
      const header = new Uint8Array([
        0x94,
        0xc3,
        (bufLen >> 8) & 0xff,
        bufLen & 0xff,
      ]);
      controller.enqueue(new Uint8Array([...header, ...chunk]));
    },
  });
};
```