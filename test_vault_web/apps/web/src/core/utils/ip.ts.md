# ip.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/ip.ts`
- **Extension:** `.ts`
- **Size:** 436 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `convertIntToIpAddress`
- `convertIpAddressToInt`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]
- [[apps/web/src/core/utils/ip.test.ts.md|apps/web/src/core/utils/ip.test.ts]]

## Source Code Snippet
```ts
export function convertIntToIpAddress(int: number): string {
  return `${int & 0xff}.${(int >> 8) & 0xff}.${(int >> 16) & 0xff}.${(int >> 24) & 0xff}`;
}

export function convertIpAddressToInt(ip: string): number | undefined {
  if (!ip) {
    return undefined;
  }
  return (
    ip
      .split(".")
      .reverse()
      .reduce((ipnum, octet) => {
        return (ipnum << 8) + Number.parseInt(octet, 10);
      }, 0) >>> 0
  );
}
```