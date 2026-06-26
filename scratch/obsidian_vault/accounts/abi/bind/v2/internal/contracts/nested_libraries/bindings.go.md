# bindings.go

## Architecture Metrics
- **Path:** `accounts/abi/bind/v2/internal/contracts/nested_libraries/bindings.go`
- **Extension:** `.go`
- **Size:** 30154 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `C1`
- `C2`
- `L1`
- `L2`
- `L2b`
- `L3`
- `L4`
- `L4b`
- `NewC1`
- `Instance`
- `PackConstructor`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewC2`
- `Instance`
- `PackConstructor`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL1`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL2`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL2b`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL3`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL4`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`
- `NewL4b`
- `Instance`
- `PackDo`
- `TryPackDo`
- `UnpackDo`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]

## Source Code Snippet
```go
// Code generated via abigen V2 - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package nested_libraries

import (
	"bytes"
	"errors"
	"math/big"

	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/accounts/abi/bind/v2"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
)

// Reference imports to suppress errors if they are not otherwise used.
var (
	_ = bytes.Equal
	_ = errors.New
...
```