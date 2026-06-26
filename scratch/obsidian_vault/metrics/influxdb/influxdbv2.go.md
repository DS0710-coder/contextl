# influxdbv2.go

## Architecture Metrics
- **Path:** `metrics/influxdb/influxdbv2.go`
- **Extension:** `.go`
- **Size:** 2454 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `v2Reporter`
- `InfluxDBV2WithTags`
- `run`
- `send`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[beacon/light/api/api_server.go.md|beacon/light/api/api_server.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package influxdb

import (
	"context"
	"time"

	"github.com/ethereum/go-ethereum/log"
	"github.com/ethereum/go-ethereum/metrics"
	influxdb2 "github.com/influxdata/influxdb-client-go/v2"
	"github.com/influxdata/influxdb-client-go/v2/api"
)

type v2Reporter struct {
	reg      metrics.Registry
	interval time.Duration

	endpoint     string
	token        string
	bucket       string
	organization string
...
```