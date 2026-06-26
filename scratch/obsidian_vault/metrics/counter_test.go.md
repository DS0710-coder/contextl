# counter_test.go

## Architecture Metrics
- **Path:** `metrics/counter_test.go`
- **Extension:** `.go`
- **Size:** 1257 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkCounter`
- `TestCounterClear`
- `TestCounter`
- `TestCounterSnapshot`
- `TestGetOrRegisterCounter`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import "testing"

func BenchmarkCounter(b *testing.B) {
	c := NewCounter()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		c.Inc(1)
	}
}

func TestCounterClear(t *testing.T) {
	c := NewCounter()
	c.Inc(1)
	c.Clear()
	if count := c.Snapshot().Count(); count != 0 {
		t.Errorf("c.Count(): 0 != %v\n", count)
	}
}
...
```