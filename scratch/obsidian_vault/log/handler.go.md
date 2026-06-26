# handler.go

## Architecture Metrics
- **Path:** `log/handler.go`
- **Extension:** `.go`
- **Size:** 5458 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `discardHandler`
- `TerminalHandler`
- `leveler`
- `DiscardHandler`
- `Handle`
- `Enabled`
- `WithGroup`
- `WithAttrs`
- `NewTerminalHandler`
- `NewTerminalHandlerWithLevel`
- `Handle`
- `Enabled`
- `WithGroup`
- `WithAttrs`
- `ResetFieldPadding`
- `Level`
- `JSONHandler`
- `JSONHandlerWithLevel`
- `LogfmtHandler`
- `LogfmtHandlerWithLevel`
- `builtinReplaceLogfmt`
- `builtinReplaceJSON`
- `builtinReplace`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"context"
	"fmt"
	"io"
	"log/slog"
	"math/big"
	"reflect"
	"sync"
	"time"

	"github.com/holiman/uint256"
)

type discardHandler struct{}

// DiscardHandler returns a no-op handler
func DiscardHandler() slog.Handler {
	return &discardHandler{}
...
```