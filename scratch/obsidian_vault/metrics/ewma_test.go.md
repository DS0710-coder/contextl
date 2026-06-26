# ewma_test.go

## Architecture Metrics
- **Path:** `metrics/ewma_test.go`
- **Extension:** `.go`
- **Size:** 2328 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkEWMA`
- `BenchmarkEWMAParallel`
- `TestEWMA1`
- `TestEWMA5`
- `TestEWMA15`
- `elapseMinute`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"math"
	"testing"
)

const epsilon = 0.0000000000000001

func BenchmarkEWMA(b *testing.B) {
	a := NewEWMA1()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		a.Update(1)
		a.tick()
	}
}

func BenchmarkEWMAParallel(b *testing.B) {
	a := NewEWMA1()
...
```