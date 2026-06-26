# json_test.go

## Architecture Metrics
- **Path:** `metrics/json_test.go`
- **Extension:** `.go`
- **Size:** 535 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestRegistryMarshallJSON`
- `TestRegistryWriteJSONOnce`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"bytes"
	"encoding/json"
	"testing"
)

func TestRegistryMarshallJSON(t *testing.T) {
	b := &bytes.Buffer{}
	enc := json.NewEncoder(b)
	r := NewRegistry()
	r.Register("counter", NewCounter())
	enc.Encode(r)
	if s := b.String(); s != "{\"counter\":{\"count\":0}}\n" {
		t.Fatal(s)
	}
}

func TestRegistryWriteJSONOnce(t *testing.T) {
...
```