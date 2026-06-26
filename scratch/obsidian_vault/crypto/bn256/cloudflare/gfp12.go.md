# gfp12.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp12.go`
- **Extension:** `.go`
- **Size:** 2954 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP12`
- `String`
- `Set`
- `SetZero`
- `SetOne`
- `IsZero`
- `IsOne`
- `Conjugate`
- `Neg`
- `Frobenius`
- `FrobeniusP2`
- `FrobeniusP4`
- `Add`
- `Sub`
- `Mul`
- `MulScalar`
- `Exp`
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

import (
	"math/big"
)

// gfP12 implements the field of size p¹² as a quadratic extension of gfP6
// where ω²=τ.
type gfP12 struct {
	x, y gfP6 // value is xω + y
}

func (e *gfP12) String() string {
	return "(" + e.x.String() + "," + e.y.String() + ")"
}

...
```