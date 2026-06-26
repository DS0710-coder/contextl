# scheduler_test.go

## Architecture Metrics
- **Path:** `beacon/light/request/scheduler_test.go`
- **Extension:** `.go`
- **Size:** 3415 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testServer`
- `testModule`
- `TestEventFilter`
- `Name`
- `subscribe`
- `canRequestNow`
- `sendRequest`
- `fail`
- `unsubscribe`
- `Process`
- `expProcess`
- `expNoMoreProcess`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package request

import (
	"reflect"
	"testing"
)

func TestEventFilter(t *testing.T) {
	s := NewScheduler()
	module1 := &testModule{name: "module1"}
	module2 := &testModule{name: "module2"}
	s.RegisterModule(module1, "module1")
	s.RegisterModule(module2, "module2")
	s.Start()
	// startup process round without events
	s.testWaitCh <- struct{}{}
	module1.expProcess(t, nil)
	module2.expProcess(t, nil)
	srv := &testServer{}
	// register server; both modules should receive server event
...
```