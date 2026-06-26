# writer_test.go

## Architecture Metrics
- **Path:** `metrics/writer_test.go`
- **Extension:** `.go`
- **Size:** 363 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestMetricsSorting`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"slices"
	"testing"
)

func TestMetricsSorting(t *testing.T) {
	var namedMetrics = []namedMetric{
		{name: "zzz"},
		{name: "bbb"},
		{name: "fff"},
		{name: "ggg"},
	}

	slices.SortFunc(namedMetrics, namedMetric.cmp)
	for i, name := range []string{"bbb", "fff", "ggg", "zzz"} {
		if namedMetrics[i].name != name {
			t.Fail()
		}
...
```