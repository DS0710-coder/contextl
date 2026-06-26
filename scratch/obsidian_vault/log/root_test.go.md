# root_test.go

## Architecture Metrics
- **Path:** `log/root_test.go`
- **Extension:** `.go`
- **Size:** 390 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `customLogger`
- `TestSetDefaultCustomLogger`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"testing"
)

// SetDefault should properly set the default logger when custom loggers are
// provided.
func TestSetDefaultCustomLogger(t *testing.T) {
	type customLogger struct {
		Logger // Implement the Logger interface
	}

	customLog := &customLogger{}
	SetDefault(customLog)
	if Root() != customLog {
		t.Error("expected custom logger to be set as default")
	}
}
```