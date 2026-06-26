# curve.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/curve.go`
- **Extension:** `.go`
- **Size:** 5689 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `curvePoint`
- `newCurvePoint`
- `String`
- `Put`
- `Set`
- `IsOnCurve`
- `SetInfinity`
- `IsInfinity`
- `Add`
- `Double`
- `Mul`
- `MakeAffine`
- `Negative`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package bn256

import (
	"math/big"
)

// curvePoint implements the elliptic curve y²=x³+3. Points are kept in
// Jacobian form and t=z² when valid. G₁ is the set of points of this curve on
// GF(p).
type curvePoint struct {
	x, y, z, t *big.Int
}

var curveB = new(big.Int).SetInt64(3)

// curveGen is the generator of G₁.
...
```