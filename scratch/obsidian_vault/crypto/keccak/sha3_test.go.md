# sha3_test.go

## Architecture Metrics
- **Path:** `crypto/keccak/sha3_test.go`
- **Extension:** `.go`
- **Size:** 5666 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `KeccakKats`
- `decodeHex`
- `TestKeccakKats`
- `TestKeccak`
- `TestUnalignedWrite`
- `sequentialBytes`
- `TestMarshalUnmarshal`
- `testMarshalUnmarshal`
- `BenchmarkPermutationFunction`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package keccak

// Tests include all the ShortMsgKATs provided by the Keccak team at
// https://github.com/gvanas/KeccakCodePackage
//
// They only include the zero-bit case of the bitwise testvectors
// published by NIST in the draft of FIPS-202.

import (
	"bytes"
	"compress/flate"
	"encoding"
	"encoding/hex"
	"encoding/json"
	"hash"
	"math/rand"
...
```