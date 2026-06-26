# counter_float_64_test.go

## Architecture Metrics
- **Path:** `metrics/counter_float_64_test.go`
- **Extension:** `.go`
- **Size:** 1580 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkCounterFloat64`
- `BenchmarkCounterFloat64Parallel`
- `TestCounterFloat64`
- `TestGetOrRegisterCounterFloat64`

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

func BenchmarkCounterFloat64(b *testing.B) {
	c := NewCounterFloat64()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		c.Inc(1.0)
	}
}

func BenchmarkCounterFloat64Parallel(b *testing.B) {
	c := NewCounterFloat64()
	b.ResetTimer()
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
...
```