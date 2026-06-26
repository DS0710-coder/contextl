# bitutil_test.go

## Architecture Metrics
- **Path:** `common/bitutil/bitutil_test.go`
- **Extension:** `.go`
- **Size:** 6338 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestXOR`
- `naiveXOR`
- `TestAND`
- `TestOR`
- `TestTest`
- `BenchmarkFastXOR1KB`
- `BenchmarkFastXOR2KB`
- `BenchmarkFastXOR4KB`
- `benchmarkFastXOR`
- `BenchmarkBaseXOR1KB`
- `BenchmarkBaseXOR2KB`
- `BenchmarkBaseXOR4KB`
- `benchmarkBaseXOR`
- `BenchmarkFastAND1KB`
- `BenchmarkFastAND2KB`
- `BenchmarkFastAND4KB`
- `benchmarkFastAND`
- `BenchmarkBaseAND1KB`
- `BenchmarkBaseAND2KB`
- `BenchmarkBaseAND4KB`
- `benchmarkBaseAND`
- `BenchmarkFastOR1KB`
- `BenchmarkFastOR2KB`
- `BenchmarkFastOR4KB`
- `benchmarkFastOR`
- `BenchmarkBaseOR1KB`
- `BenchmarkBaseOR2KB`
- `BenchmarkBaseOR4KB`
- `benchmarkBaseOR`
- `BenchmarkFastTest1KB`
- `BenchmarkFastTest2KB`
- `BenchmarkFastTest4KB`
- `benchmarkFastTest`
- `BenchmarkBaseTest1KB`
- `BenchmarkBaseTest2KB`
- `BenchmarkBaseTest4KB`
- `benchmarkBaseTest`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2013 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Adapted from: https://go.dev/src/crypto/subtle/xor_test.go

package bitutil

import (
	"bytes"
	"testing"
)

// Tests that bitwise XOR works for various alignments.
func TestXOR(t *testing.T) {
	for alignP := 0; alignP < 2; alignP++ {
		for alignQ := 0; alignQ < 2; alignQ++ {
			for alignD := 0; alignD < 2; alignD++ {
				p := make([]byte, 1023)[alignP:]
				q := make([]byte, 1023)[alignQ:]
...
```