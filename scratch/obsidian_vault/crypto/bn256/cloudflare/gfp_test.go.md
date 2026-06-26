# gfp_test.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp_test.go`
- **Extension:** `.go`
- **Size:** 2029 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestGFpNeg`
- `TestGFpAdd`
- `TestGFpSub`
- `TestGFpMul`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"testing"
)

// Tests that negation works the same way on both assembly-optimized and pure Go
// implementation.
func TestGFpNeg(t *testing.T) {
	n := &gfP{0x0123456789abcdef, 0xfedcba9876543210, 0xdeadbeefdeadbeef, 0xfeebdaedfeebdaed}
	w := &gfP{0xfedcba9876543211, 0x0123456789abcdef, 0x2152411021524110, 0x0114251201142512}
	h := &gfP{}

	gfpNeg(h, n)
	if *h != *w {
		t.Errorf("negation mismatch: have %#x, want %#x", *h, *w)
	}
}

// Tests that addition works the same way on both assembly-optimized and pure Go
...
```