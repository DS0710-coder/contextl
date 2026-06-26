# gfp12.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/gfp12.go`
- **Extension:** `.go`
- **Size:** 3645 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfP12`
- `newGFp12`
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
- `Frobenius`
- `FrobeniusP2`
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

// gfP12 implements the field of size p¹² as a quadratic extension of gfP6
// where ω²=τ.
type gfP12 struct {
	x, y *gfP6 // value is xω + y
}

...
```