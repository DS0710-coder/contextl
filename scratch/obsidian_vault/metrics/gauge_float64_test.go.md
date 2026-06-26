# gauge_float64_test.go

## Architecture Metrics
- **Path:** `metrics/gauge_float64_test.go`
- **Extension:** `.go`
- **Size:** 1014 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkGaugeFloat64`
- `BenchmarkGaugeFloat64Parallel`
- `TestGaugeFloat64Snapshot`
- `TestGetOrRegisterGaugeFloat64`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"sync"
	"testing"
)

func BenchmarkGaugeFloat64(b *testing.B) {
	g := NewGaugeFloat64()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		g.Update(float64(i))
	}
}

func BenchmarkGaugeFloat64Parallel(b *testing.B) {
	c := NewGaugeFloat64()
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
...
```