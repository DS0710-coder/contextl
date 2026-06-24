# deepCompareConfig.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/deepCompareConfig.ts`
- **Extension:** `.ts`
- **Size:** 1698 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `isObject`
- `isUint8Array`
- `bytesEqual`
- `deepCompareConfig`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx]]
- [[apps/web/src/core/utils/deepCompareConfig.test.ts.md|apps/web/src/core/utils/deepCompareConfig.test.ts]]

## Source Code Snippet
```ts
function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function isUint8Array(v: unknown): v is Uint8Array {
  return v instanceof Uint8Array;
}

function bytesEqual(a: Uint8Array, b: Uint8Array): boolean {
  if (a.byteLength !== b.byteLength) {
    return false;
  }
  for (let i = 0; i < a.byteLength; i++) {
    if (a[i] !== b[i]) {
      return false;
    }
  }
  return true;
}

...
```