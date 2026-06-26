# logger.go

## Architecture Metrics
- **Path:** `log/logger.go`
- **Extension:** `.go`
- **Size:** 5336 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Logger`
- `logger`
- `FromLegacyLevel`
- `LevelAlignedString`
- `LevelString`
- `NewLogger`
- `Handler`
- `Write`
- `Log`
- `With`
- `New`
- `Enabled`
- `Trace`
- `Debug`
- `Info`
- `Warn`
- `Error`
- `Crit`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"context"
	"log/slog"
	"math"
	"os"
	"runtime"
	"time"
)

const errorKey = "LOG_ERROR"

const (
	legacyLevelCrit = iota
	legacyLevelError
	legacyLevelWarn
	legacyLevelInfo
	legacyLevelDebug
	legacyLevelTrace
...
```