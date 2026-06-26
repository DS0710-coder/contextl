# bn256_slow.go

## Architecture Metrics
- **Path:** `crypto/bn256/bn256_slow.go`
- **Extension:** `.go`
- **Size:** 850 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PairingCheck`

## Imports (Dependencies)
- [[crypto/bn256/google/bn256.go.md|crypto/bn256/google/bn256.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 Péter Szilágyi. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be found
// in the LICENSE file.

//go:build !amd64 && !arm64
// +build !amd64,!arm64

// Package bn256 implements the Optimal Ate pairing over a 256-bit Barreto-Naehrig curve.
package bn256

import bn256 "github.com/ethereum/go-ethereum/crypto/bn256/google"

// G1 is an abstract cyclic group. The zero value is suitable for use as the
// output of an operation, but cannot be used as an input.
type G1 = bn256.G1

// G2 is an abstract cyclic group. The zero value is suitable for use as the
// output of an operation, but cannot be used as an input.
type G2 = bn256.G2

...
```