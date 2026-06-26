# gfp6.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp6.go`
- **Extension:** `.go`
- **Size:** 4625 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP6`
- `String`
- `Set`
- `SetZero`
- `SetOne`
- `IsZero`
- `IsOne`
- `Neg`
- `Frobenius`
- `FrobeniusP2`
- `FrobeniusP4`
- `Add`
- `Sub`
- `Mul`
- `MulScalar`
- `MulGFP`
- `MulTau`
- `Square`
- `Invert`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

// For details of the algorithms used, see "Multiplication and Squaring on
// Pairing-Friendly Fields, Devegili et al.
// http://eprint.iacr.org/2006/471.pdf.

// gfP6 implements the field of size p⁶ as a cubic extension of gfP2 where τ³=ξ
// and ξ=i+9.
type gfP6 struct {
	x, y, z gfP2 // value is xτ² + yτ + z
}

func (e *gfP6) String() string {
	return "(" + e.x.String() + ", " + e.y.String() + ", " + e.z.String() + ")"
}

func (e *gfP6) Set(a *gfP6) *gfP6 {
	e.x.Set(&a.x)
	e.y.Set(&a.y)
	e.z.Set(&a.z)
...
```