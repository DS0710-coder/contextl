# influxdbv1.go

## Architecture Metrics
- **Path:** `metrics/influxdb/influxdbv1.go`
- **Extension:** `.go`
- **Size:** 3797 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `reporter`
- `InfluxDB`
- `InfluxDBWithTags`
- `InfluxDBWithTagsOnce`
- `makeClient`
- `run`
- `send`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package influxdb

import (
	"fmt"
	uurl "net/url"
	"time"

	"github.com/ethereum/go-ethereum/log"
	"github.com/ethereum/go-ethereum/metrics"
	client "github.com/influxdata/influxdb1-client/v2"
)

type reporter struct {
	reg      metrics.Registry
	interval time.Duration

	url       uurl.URL
	database  string
	username  string
	password  string
...
```