# gfp2.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/gfp2.go`
- **Extension:** `.go`
- **Size:** 3888 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP2`
- `newGFp2`
- `String`
- `Put`
- `Set`
- `SetZero`
- `SetOne`
- `Minimal`
- `IsZero`
- `IsOne`
- `Conjugate`
- `Negative`
- `Add`
- `Sub`
- `Double`
- `Exp`
- `Mul`
- `MulScalar`
- `MulXi`
- `Square`
- `Invert`
- `Real`
- `Imag`

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

// For details of the algorithms used, see "Multiplication and Squaring on
// Pairing-Friendly Fields, Devegili et al.
// http://eprint.iacr.org/2006/471.pdf.

import (
	"math/big"
)

// gfP2 implements a field of size p² as a quadratic extension of the base
// field where i²=-1.
type gfP2 struct {
	x, y *big.Int // value is xi+y.
}

...
```