# scalar_mult_cgo.go

## Architecture Metrics
- **Path:** `crypto/secp256k1/scalar_mult_cgo.go`
- **Extension:** `.go`
- **Size:** 1445 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ScalarMult`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 Jeffrey Wilcke, Felix Lange, Gustav Simonsson. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be found in
// the LICENSE file.

//go:build !gofuzz && cgo
// +build !gofuzz,cgo

package secp256k1

import (
	"math/big"
	"unsafe"

	"github.com/ethereum/go-ethereum/common/math"
)

/*

#include "libsecp256k1/include/secp256k1.h"

...
```