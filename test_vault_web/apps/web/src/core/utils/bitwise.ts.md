# bitwise.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/bitwise.ts`
- **Extension:** `.ts`
- **Size:** 417 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EnumLike`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
export interface EnumLike {
  [key: number]: string | number;
}

export const bitwiseEncode = (enumValues: number[]): number => {
  return enumValues.reduce((acc, curr) => acc | curr, 0);
};

export const bitwiseDecode = (
  value: number,
  decodeEnum: EnumLike,
): number[] => {
  const enumValues = Object.keys(decodeEnum).map(Number).filter(Boolean);
  return enumValues.map((b) => value & b).filter(Boolean);
};
```