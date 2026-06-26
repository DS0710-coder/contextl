# gauge_info.go

## Architecture Metrics
- **Path:** `metrics/gauge_info.go`
- **Extension:** `.go`
- **Size:** 1536 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GaugeInfo`
- `String`
- `GetOrRegisterGaugeInfo`
- `NewGaugeInfo`
- `NewRegisteredGaugeInfo`
- `Value`
- `Snapshot`
- `Update`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"encoding/json"
	"sync"
)

// GaugeInfoValue is a mapping of keys to values
type GaugeInfoValue map[string]string

func (val GaugeInfoValue) String() string {
	data, _ := json.Marshal(val)
	return string(data)
}

// GetOrRegisterGaugeInfo returns an existing GaugeInfo or constructs and registers a
// new GaugeInfo.
func GetOrRegisterGaugeInfo(name string, r Registry) *GaugeInfo {
	if r == nil {
		r = DefaultRegistry
...
```