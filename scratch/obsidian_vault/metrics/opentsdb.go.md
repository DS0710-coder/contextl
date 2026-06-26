# opentsdb.go

## Architecture Metrics
- **Path:** `metrics/opentsdb.go`
- **Extension:** `.go`
- **Size:** 6016 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `OpenTSDBConfig`
- `OpenTSDB`
- `OpenTSDBWithConfig`
- `getShortHostname`
- `writeRegistry`
- `openTSDB`

## Imports (Dependencies)
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"strings"
	"time"
)

var shortHostName = ""

// OpenTSDBConfig provides a container with configuration parameters for
// the OpenTSDB exporter
type OpenTSDBConfig struct {
	Addr          *net.TCPAddr  // Network address to connect to
	Registry      Registry      // Registry to be exported
...
```