# mul_arm64.h

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/mul_arm64.h`
- **Extension:** `.h`
- **Size:** 2615 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```h
// mul multiplies two 256-bit numbers in little-endian order.
// The inputs are (R1,R2,R3,R4) times (R5,R6,R7,R8)
// and the product is stored in (c0,c1,c2,c3,c4,c5,c6,c7).
// Note that the input registers (R1,R2,R3) are overwritten.
#define mul(c0,c1,c2,c3,c4,c5,c6,c7) \
	MUL R1, R5, c0 \
	UMULH R1, R5, c1 \
	MUL R1, R6, R0 \
	ADDS R0, c1 \
	UMULH R1, R6, c2 \
	MUL R1, R7, R0 \
	ADCS R0, c2 \
	UMULH R1, R7, c3 \
	MUL R1, R8, R0 \
	ADCS R0, c3 \
	UMULH R1, R8, c4 \
	ADCS ZR, c4 \
	\
	MUL R2, R5, R1 \
	UMULH R2, R5, R26 \
...
```