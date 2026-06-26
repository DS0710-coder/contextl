# blake2b_f_fuzz_test.go

## Architecture Metrics
- **Path:** `crypto/blake2b/blake2b_f_fuzz_test.go`
- **Extension:** `.go`
- **Size:** 1552 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Fuzz`
- `fuzz`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Only enable fuzzer on platforms with AVX enabled
//go:build go1.7 && amd64 && !gccgo && !appengine
// +build go1.7,amd64,!gccgo,!appengine

package blake2b

import (
	"encoding/binary"
	"testing"
)

func Fuzz(f *testing.F) {
	f.Fuzz(func(t *testing.T, data []byte) {
		fuzz(data)
	})
}

func fuzz(data []byte) {
	// Make sure the data confirms to the input model
	if len(data) != 211 {
...
```