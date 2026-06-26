# blake2b_test.go

## Architecture Metrics
- **Path:** `crypto/blake2b/blake2b_test.go`
- **Extension:** `.go`
- **Size:** 110711 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestHashes`
- `TestHashes2X`
- `TestMarshal`
- `testHashes`
- `testHashes2X`
- `generateSequence`
- `computeMAC`
- `computeHash`
- `TestSelfTest`
- `benchmarkSum`
- `benchmarkWrite`
- `BenchmarkWrite128Generic`
- `BenchmarkWrite1KGeneric`
- `BenchmarkWrite128SSE4`
- `BenchmarkWrite1KSSE4`
- `BenchmarkWrite128AVX`
- `BenchmarkWrite1KAVX`
- `BenchmarkWrite128AVX2`
- `BenchmarkWrite1KAVX2`
- `BenchmarkSum128Generic`
- `BenchmarkSum1KGeneric`
- `BenchmarkSum128SSE4`
- `BenchmarkSum1KSSE4`
- `BenchmarkSum128AVX`
- `BenchmarkSum1KAVX`
- `BenchmarkSum128AVX2`
- `BenchmarkSum1KAVX2`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package blake2b

import (
	"bytes"
	"encoding"
	"encoding/hex"
	"fmt"
	"hash"
	"io"
	"testing"
)

func TestHashes(t *testing.T) {
	defer func(sse4, avx, avx2 bool) {
		useSSE4, useAVX, useAVX2 = sse4, avx, avx2
	}(useSSE4, useAVX, useAVX2)
...
```