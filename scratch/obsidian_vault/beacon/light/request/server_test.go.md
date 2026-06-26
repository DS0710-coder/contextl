# server_test.go

## Architecture Metrics
- **Path:** `beacon/light/request/server_test.go`
- **Extension:** `.go`
- **Size:** 5740 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testRequestServer`
- `TestServerEvents`
- `TestServerParallel`
- `TestServerFail`
- `TestServerEventRateLimit`
- `TestServerUnsubscribe`
- `Name`
- `Subscribe`
- `SendRequest`
- `Unsubscribe`

## Imports (Dependencies)
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package request

import (
	"testing"

	"github.com/ethereum/go-ethereum/common/mclock"
)

const (
	testRequest  = "Life, the Universe, and Everything"
	testResponse = 42
)

var testEventType = &EventType{Name: "testEvent"}

func TestServerEvents(t *testing.T) {
	rs := &testRequestServer{}
	clock := &mclock.Simulated{}
	srv := NewServer(rs, clock)
	var lastEventType *EventType
...
```