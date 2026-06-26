# gauge_info_test.go

## Architecture Metrics
- **Path:** `metrics/gauge_info_test.go`
- **Extension:** `.go`
- **Size:** 949 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestGaugeInfoJsonString`
- `TestGetOrRegisterGaugeInfo`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"testing"
)

func TestGaugeInfoJsonString(t *testing.T) {
	g := NewGaugeInfo()
	g.Update(GaugeInfoValue{
		"chain_id":   "5",
		"anotherKey": "any_string_value",
		"third_key":  "anything",
	},
	)
	want := `{"anotherKey":"any_string_value","chain_id":"5","third_key":"anything"}`

	original := g.Snapshot()
	g.Update(GaugeInfoValue{"value": "updated"})

	if have := original.Value().String(); have != want {
...
```