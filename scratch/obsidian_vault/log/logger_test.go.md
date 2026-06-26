# logger_test.go

## Architecture Metrics
- **Path:** `log/logger_test.go`
- **Extension:** `.go`
- **Size:** 7462 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `custom`
- `TestLoggingWithVmodule`
- `TestLoggingWithVmoduleDowngrade`
- `TestWithAttrsVerbosityChange`
- `TestTerminalHandlerWithAttrs`
- `TestJSONHandler`
- `BenchmarkTraceLogging`
- `BenchmarkTerminalHandler`
- `BenchmarkLogfmtHandler`
- `BenchmarkJSONHandler`
- `benchmarkLogger`
- `TestLoggerOutput`
- `BenchmarkAppendFormat`
- `TestTermTimeFormat`

## Imports (Dependencies)
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"math/big"
	"strings"
	"testing"
	"time"

	"github.com/holiman/uint256"
)

// TestLoggingWithVmodule checks that vmodule works.
func TestLoggingWithVmodule(t *testing.T) {
	out := new(bytes.Buffer)
	glog := NewGlogHandler(NewTerminalHandlerWithLevel(out, LevelTrace, false))
...
```