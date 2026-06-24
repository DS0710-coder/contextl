# ip.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/ip.test.ts`
- **Extension:** `.ts`
- **Size:** 2161 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/ip.ts.md|apps/web/src/core/utils/ip.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { convertIntToIpAddress, convertIpAddressToInt } from "./ip.ts";

describe("IP Address Conversion Functions", () => {
  describe("convertIntToIpAddress", () => {
    it("converts 0 to 0.0.0.0", () => {
      expect(convertIntToIpAddress(0)).toBe("0.0.0.0");
    });

    it("converts 16_777_343  to 127.0.0.1", () => {
      expect(convertIntToIpAddress(16_777_343)).toBe("127.0.0.1");
    });

    it("converts  16_820_416 to 192.168.0.1", () => {
      expect(convertIntToIpAddress(16_820_416)).toBe("192.168.0.1");
    });

    it("converts 4_294_967_295 to 255.255.255.255", () => {
      expect(convertIntToIpAddress(4_294_967_295)).toBe("255.255.255.255");
    });
...
```