# fromDevice.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/packet-codec/fromDevice.ts`
- **Extension:** `.ts`
- **Size:** 2273 bytes
- **Centrality Score:** 0.0049
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/packet-codec/index.ts.md|packages/sdk/src/core/packet-codec/index.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/shim/legacyUtils.ts.md|packages/sdk/src/shim/legacyUtils.ts]]

## Source Code Snippet
```ts
import type { DeviceOutput } from "../transport/Transport.ts";

/**
 * Transforms a raw byte stream from the device into typed DeviceOutput chunks
 * by parsing the 0x94 0xC3 framing header and length prefix.
 */
export const fromDeviceStream: () => TransformStream<
  Uint8Array,
  DeviceOutput
> = () => {
  let byteBuffer = new Uint8Array([]);
  const textDecoder = new TextDecoder();
  return new TransformStream<Uint8Array, DeviceOutput>({
    transform(chunk: Uint8Array, controller): void {
      byteBuffer = new Uint8Array([...byteBuffer, ...chunk]);
      let processingExhausted = false;
      while (byteBuffer.length !== 0 && !processingExhausted) {
        const framingIndex = byteBuffer.indexOf(0x94);
        const framingByte2 = byteBuffer[framingIndex + 1];
        if (framingByte2 === 0xc3) {
...
```