# histogram_test.go

## Architecture Metrics
- **Path:** `metrics/histogram_test.go`
- **Extension:** `.go`
- **Size:** 2362 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkHistogram`
- `TestGetOrRegisterHistogram`
- `TestHistogram10000`
- `TestHistogramEmpty`
- `TestHistogramSnapshot`
- `testHistogram10000`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import "testing"

func BenchmarkHistogram(b *testing.B) {
	h := NewHistogram(NewUniformSample(100))
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		h.Update(int64(i))
	}
}

func TestGetOrRegisterHistogram(t *testing.T) {
	r := NewRegistry()
	s := NewUniformSample(100)
	NewRegisteredHistogram("foo", r, s).Update(47)
	if h := GetOrRegisterHistogram("foo", r, s).Snapshot(); h.Count() != 1 {
		t.Fatal(h)
	}
}
...
```