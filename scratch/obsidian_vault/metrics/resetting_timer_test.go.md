# resetting_timer_test.go

## Architecture Metrics
- **Path:** `metrics/resetting_timer_test.go`
- **Extension:** `.go`
- **Size:** 4657 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestResettingTimer`
- `TestResettingTimerWithFivePercentiles`

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

func TestResettingTimer(t *testing.T) {
	tests := []struct {
		values   []int64
		start    int
		end      int
		wantP50  float64
		wantP95  float64
		wantP99  float64
		wantMean float64
		wantMin  int64
		wantMax  int64
	}{
		{
...
```