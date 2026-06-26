# bn256_test.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/bn256_test.go`
- **Extension:** `.go`
- **Size:** 6751 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestGFp2Invert`
- `isZero`
- `isOne`
- `TestGFp6Invert`
- `TestGFp12Invert`
- `TestCurveImpl`
- `TestOrderG1`
- `TestOrderG2`
- `TestOrderGT`
- `TestBilinearity`
- `TestG1Marshal`
- `TestG2Marshal`
- `TestG1Identity`
- `TestG2Identity`
- `TestTripartiteDiffieHellman`
- `BenchmarkPairing`

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
	"bytes"
	"crypto/rand"
	"math/big"
	"testing"
)

func TestGFp2Invert(t *testing.T) {
	pool := new(bnPool)

	a := newGFp2(pool)
	a.x.SetString("23423492374", 10)
	a.y.SetString("12934872398472394827398470", 10)

...
```