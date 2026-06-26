# opentsdb_test.go

## Architecture Metrics
- **Path:** `metrics/opentsdb_test.go`
- **Extension:** `.go`
- **Size:** 1695 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ExampleOpenTSDB`
- `ExampleOpenTSDBWithConfig`
- `TestExampleOpenTSB`
- `findFirstDiffPos`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"fmt"
	"net"
	"os"
	"strings"
	"testing"
	"time"
)

func ExampleOpenTSDB() {
	addr, _ := net.ResolveTCPAddr("net", ":2003")
	go OpenTSDB(DefaultRegistry, 1*time.Second, "some.prefix", addr)
}

func ExampleOpenTSDBWithConfig() {
	addr, _ := net.ResolveTCPAddr("net", ":2003")
	go OpenTSDBWithConfig(OpenTSDBConfig{
		Addr:          addr,
...
```