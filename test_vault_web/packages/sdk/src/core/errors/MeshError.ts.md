# MeshError.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/errors/MeshError.ts`
- **Extension:** `.ts`
- **Size:** 522 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MeshError`
- `TransportClosedError`
- `PacketTooLargeError`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export class MeshError extends Error {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = "MeshError";
  }
}

export class TransportClosedError extends MeshError {
  constructor() {
    super("Transport is closed");
    this.name = "TransportClosedError";
  }
}

export class PacketTooLargeError extends MeshError {
  constructor(size: number) {
    super(`Message longer than 512 bytes (got ${size}), it will not be sent!`);
    this.name = "PacketTooLargeError";
  }
}
```