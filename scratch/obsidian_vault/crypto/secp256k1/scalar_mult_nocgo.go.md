# scalar_mult_nocgo.go

## Architecture Metrics
- **Path:** `crypto/secp256k1/scalar_mult_nocgo.go`
- **Extension:** `.go`
- **Size:** 446 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ScalarMult`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 Jeffrey Wilcke, Felix Lange, Gustav Simonsson. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be found in
// the LICENSE file.

//go:build gofuzz || !cgo
// +build gofuzz !cgo

package secp256k1

import "math/big"

func (bitCurve *BitCurve) ScalarMult(Bx, By *big.Int, scalar []byte) (*big.Int, *big.Int) {
	panic("ScalarMult is not available when secp256k1 is built without cgo")
}
```