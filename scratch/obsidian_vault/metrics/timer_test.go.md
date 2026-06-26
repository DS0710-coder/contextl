# timer_test.go

## Architecture Metrics
- **Path:** `metrics/timer_test.go`
- **Extension:** `.go`
- **Size:** 2678 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkTimer`
- `TestGetOrRegisterTimer`
- `TestTimerExtremes`
- `TestTimerStop`
- `TestTimerFunc`
- `TestTimerZero`
- `ExampleGetOrRegisterTimer`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"fmt"
	"math"
	"testing"
	"time"
)

func BenchmarkTimer(b *testing.B) {
	tm := NewTimer()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tm.Update(1)
	}
}

func TestGetOrRegisterTimer(t *testing.T) {
	r := NewRegistry()
	NewRegisteredTimer("foo", r).Update(47)
...
```