# twist.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/twist.go`
- **Extension:** `.go`
- **Size:** 4269 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `twistPoint`
- `String`
- `Set`
- `IsOnCurve`
- `SetInfinity`
- `IsInfinity`
- `Add`
- `Double`
- `Mul`
- `MakeAffine`
- `Neg`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"math/big"
)

// twistPoint implements the elliptic curve y²=x³+3/ξ over GF(p²). Points are
// kept in Jacobian form and t=z² when valid. The group G₂ is the set of
// n-torsion points of this curve over GF(p²) (where n = Order)
type twistPoint struct {
	x, y, z, t gfP2
}

var twistB = &gfP2{
	gfP{0x38e7ecccd1dcff67, 0x65f0b37d93ce0d3e, 0xd749d0dd22ac00aa, 0x0141b9ce4a688d4d},
	gfP{0x3bf938e377b802a8, 0x020b1b273633535d, 0x26b7edf049755260, 0x2514c6324384a86d},
}

// twistGen is the generator of group G₂.
var twistGen = &twistPoint{
...
```