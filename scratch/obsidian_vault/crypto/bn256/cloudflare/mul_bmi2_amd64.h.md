# mul_bmi2_amd64.h

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/mul_bmi2_amd64.h`
- **Extension:** `.h`
- **Size:** 2058 bytes
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
#define mulBMI2(a0,a1,a2,a3, rb) \
	MOVQ a0, DX \
	MOVQ $0, R13 \
	MULXQ 0+rb, R8, R9 \
	MULXQ 8+rb, AX, R10 \
	ADDQ AX, R9 \
	MULXQ 16+rb, AX, R11 \
	ADCQ AX, R10 \
	MULXQ 24+rb, AX, R12 \
	ADCQ AX, R11 \
	ADCQ $0, R12 \
	ADCQ $0, R13 \
	\
	MOVQ a1, DX \
	MOVQ $0, R14 \
	MULXQ 0+rb, AX, BX \
	ADDQ AX, R9 \
	ADCQ BX, R10 \
	MULXQ 16+rb, AX, BX \
	ADCQ AX, R11 \
...
```