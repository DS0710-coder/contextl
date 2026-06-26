# gfp2.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp2.go`
- **Extension:** `.go`
- **Size:** 2861 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP2`
- `gfP2Decode`
- `String`
- `Set`
- `SetZero`
- `SetOne`
- `IsZero`
- `IsOne`
- `Conjugate`
- `Neg`
- `Add`
- `Sub`
- `Mul`
- `MulScalar`
- `MulXi`
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

// gfP2 implements a field of size p² as a quadratic extension of the base field
// where i²=-1.
type gfP2 struct {
	x, y gfP // value is xi+y.
}

func gfP2Decode(in *gfP2) *gfP2 {
	out := &gfP2{}
	montDecode(&out.x, &in.x)
	montDecode(&out.y, &in.y)
	return out
}

func (e *gfP2) String() string {
...
```