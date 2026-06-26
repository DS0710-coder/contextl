# config_test.go

## Architecture Metrics
- **Path:** `beacon/params/config_test.go`
- **Extension:** `.go`
- **Size:** 774 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestChainConfig_LoadForks`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package params

import (
	"bytes"
	"testing"
)

func TestChainConfig_LoadForks(t *testing.T) {
	const config = `
GENESIS_FORK_VERSION: 0x00000000

ALTAIR_FORK_VERSION: 0x00000001
ALTAIR_FORK_EPOCH: 1

EIP7928_FORK_VERSION: 0xb0000038
EIP7928_FORK_EPOCH: 18446744073709551615

EIP7XXX_FORK_VERSION: 
EIP7XXX_FORK_EPOCH: 

...
```