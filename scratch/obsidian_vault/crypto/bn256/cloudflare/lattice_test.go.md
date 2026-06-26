# lattice_test.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/lattice_test.go`
- **Extension:** `.go`
- **Size:** 731 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestLatticeReduceCurve`
- `TestLatticeReduceTarget`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"crypto/rand"

	"testing"
)

func TestLatticeReduceCurve(t *testing.T) {
	k, _ := rand.Int(rand.Reader, Order)
	ks := curveLattice.decompose(k)

	if ks[0].BitLen() > 130 || ks[1].BitLen() > 130 {
		t.Fatal("reduction too large")
	} else if ks[0].Sign() < 0 || ks[1].Sign() < 0 {
		t.Fatal("reduction must be positive")
	}
}

func TestLatticeReduceTarget(t *testing.T) {
...
```