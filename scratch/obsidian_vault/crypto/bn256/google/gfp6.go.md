# gfp6.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/gfp6.go`
- **Extension:** `.go`
- **Size:** 5784 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP6`
- `newGFp6`
- `String`
- `Put`
- `Set`
- `SetZero`
- `SetOne`
- `Minimal`
- `IsZero`
- `IsOne`
- `Negative`
- `Frobenius`
- `FrobeniusP2`
- `Add`
- `Sub`
- `Double`
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

// gfP6 implements the field of size p⁶ as a cubic extension of gfP2 where τ³=ξ
// and ξ=i+9.
type gfP6 struct {
	x, y, z *gfP2 // value is xτ² + yτ + z
}

...
```