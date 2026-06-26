# meter_test.go

## Architecture Metrics
- **Path:** `metrics/meter_test.go`
- **Extension:** `.go`
- **Size:** 1709 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkMeter`
- `TestMeter`
- `TestGetOrRegisterMeter`
- `TestMeterDecay`
- `TestMeterNonzero`
- `TestMeterStop`
- `TestMeterZero`
- `TestMeterRepeat`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"testing"
	"time"
)

func BenchmarkMeter(b *testing.B) {
	m := NewMeter()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		m.Mark(1)
	}
}
func TestMeter(t *testing.T) {
	m := NewMeter()
	m.Mark(47)
	if v := m.Snapshot().Count(); v != 47 {
		t.Fatalf("have %d want %d", v, 47)
	}
...
```