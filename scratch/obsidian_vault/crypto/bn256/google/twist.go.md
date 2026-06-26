# twist.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/twist.go`
- **Extension:** `.go`
- **Size:** 5745 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `twistPoint`
- `newTwistPoint`
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

// twistPoint implements the elliptic curve y²=x³+3/ξ over GF(p²). Points are
// kept in Jacobian form and t=z² when valid. The group G₂ is the set of
// n-torsion points of this curve over GF(p²) (where n = Order)
type twistPoint struct {
	x, y, z, t *gfP2
}

var twistB = &gfP2{
	bigFromBase10("266929791119991161246907387137283842545076965332900288569378510910307636690"),
	bigFromBase10("19485874751759354771024239261021720505790618469301721065564631296452457478373"),
...
```