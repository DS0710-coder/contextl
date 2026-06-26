# curve.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/curve.go`
- **Extension:** `.go`
- **Size:** 4702 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `curvePoint`
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

// curvePoint implements the elliptic curve y²=x³+3. Points are kept in Jacobian
// form and t=z² when valid. G₁ is the set of points of this curve on GF(p).
type curvePoint struct {
	x, y, z, t gfP
}

var curveB = newGFp(3)

// curveGen is the generator of G₁.
var curveGen = &curvePoint{
	x: *newGFp(1),
	y: *newGFp(2),
	z: *newGFp(1),
	t: *newGFp(1),
...
```