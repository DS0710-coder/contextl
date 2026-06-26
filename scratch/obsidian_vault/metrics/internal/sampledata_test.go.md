# sampledata_test.go

## Architecture Metrics
- **Path:** `metrics/internal/sampledata_test.go`
- **Extension:** `.go`
- **Size:** 629 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestCollectRuntimeMetrics`

## Imports (Dependencies)
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package internal

import (
	"bytes"
	"encoding/gob"
	"fmt"
	metrics2 "runtime/metrics"
	"testing"
	"time"

	"github.com/ethereum/go-ethereum/metrics"
)

func TestCollectRuntimeMetrics(t *testing.T) {
	t.Skip("Only used for generating testdata")
	serialize := func(path string, histogram *metrics2.Float64Histogram) {
		var f = new(bytes.Buffer)
		if err := gob.NewEncoder(f).Encode(histogram); err != nil {
			panic(err)
		}
...
```