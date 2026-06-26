# gfp_generic.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp_generic.go`
- **Extension:** `.go`
- **Size:** 3285 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfpCarry`
- `gfpNeg`
- `gfpAdd`
- `gfpSub`
- `mul`
- `halfMul`
- `gfpMul`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
//go:build (!amd64 && !arm64) || generic
// +build !amd64,!arm64 generic

package bn256

func gfpCarry(a *gfP, head uint64) {
	b := &gfP{}

	var carry uint64
	for i, pi := range p2 {
		ai := a[i]
		bi := ai - pi - carry
		b[i] = bi
		carry = (pi&^ai | (pi|^ai)&bi) >> 63
	}
	carry = carry &^ head

	// If b is negative, then return a.
	// Else return b.
	carry = -carry
...
```