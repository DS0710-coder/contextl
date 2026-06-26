# mul_amd64.h

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/mul_amd64.h`
- **Extension:** `.h`
- **Size:** 3120 bytes
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
#define mul(a0,a1,a2,a3, rb, stack) \
	MOVQ a0, AX \
	MULQ 0+rb \
	MOVQ AX, R8 \
	MOVQ DX, R9 \
	MOVQ a0, AX \
	MULQ 8+rb \
	ADDQ AX, R9 \
	ADCQ $0, DX \
	MOVQ DX, R10 \
	MOVQ a0, AX \
	MULQ 16+rb \
	ADDQ AX, R10 \
	ADCQ $0, DX \
	MOVQ DX, R11 \
	MOVQ a0, AX \
	MULQ 24+rb \
	ADDQ AX, R11 \
	ADCQ $0, DX \
	MOVQ DX, R12 \
...
```