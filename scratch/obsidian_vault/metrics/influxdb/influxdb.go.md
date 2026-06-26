# influxdb.go

## Architecture Metrics
- **Path:** `metrics/influxdb/influxdb.go`
- **Extension:** `.go`
- **Size:** 3280 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `readMeter`

## Imports (Dependencies)
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]

## Source Code Snippet
```go
package influxdb

import (
	"fmt"

	"github.com/ethereum/go-ethereum/metrics"
)

func readMeter(namespace, name string, i interface{}) (string, map[string]interface{}) {
	switch metric := i.(type) {
	case *metrics.Counter:
		measurement := fmt.Sprintf("%s%s.count", namespace, name)
		fields := map[string]interface{}{
			"value": metric.Snapshot().Count(),
		}
		return measurement, fields
	case *metrics.CounterFloat64:
		measurement := fmt.Sprintf("%s%s.count", namespace, name)
		fields := map[string]interface{}{
			"value": metric.Snapshot().Count(),
...
```