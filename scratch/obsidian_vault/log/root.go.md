# root.go

## Architecture Metrics
- **Path:** `log/root.go`
- **Extension:** `.go`
- **Size:** 2852 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `init`
- `SetDefault`
- `Root`
- `Trace`
- `Debug`
- `Info`
- `Warn`
- `Error`
- `Crit`
- `New`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"log/slog"
	"os"
	"sync"
)

var (
	rootLock sync.RWMutex
	root     Logger
)

func init() {
	root = &logger{slog.New(DiscardHandler())}
}

// SetDefault sets the default global logger
func SetDefault(l Logger) {
	rootLock.Lock()
...
```