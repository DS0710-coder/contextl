# registry.go

## Architecture Metrics
- **Path:** `metrics/registry.go`
- **Extension:** `.go`
- **Size:** 10330 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Registry`
- `orderedRegistry`
- `StandardRegistry`
- `Stoppable`
- `PrefixedRegistry`
- `Each`
- `NewRegistry`
- `NewOrderedRegistry`
- `Each`
- `Get`
- `GetOrRegister`
- `Register`
- `RunHealthchecks`
- `GetAll`
- `Unregister`
- `loadOrRegister`
- `registered`
- `stop`
- `NewPrefixedRegistry`
- `NewPrefixedChildRegistry`
- `Each`
- `findPrefix`
- `Get`
- `GetOrRegister`
- `Register`
- `RunHealthchecks`
- `GetAll`
- `Unregister`
- `Each`
- `Get`
- `GetOrRegister`
- `Register`
- `MustRegister`
- `RunHealthchecks`
- `Unregister`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"errors"
	"fmt"
	"sort"
	"strings"
	"sync"
)

// ErrDuplicateMetric is the error returned by Registry.Register when a metric
// already exists. If you mean to Register that metric you must first
// Unregister the existing metric.
var ErrDuplicateMetric = errors.New("duplicate metric")

// A Registry holds references to a set of metrics by name and can iterate
// over them, calling callback functions provided by the user.
//
// This is an interface to encourage other structs to implement
// the Registry API as appropriate.
...
```