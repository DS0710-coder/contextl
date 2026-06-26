# bindings.go

## Architecture Metrics
- **Path:** `accounts/abi/bind/v2/internal/contracts/db/bindings.go`
- **Extension:** `.go`
- **Size:** 16574 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DBStats`
- `DB`
- `GetNamedStatParamsOutput`
- `GetStatParamsOutput`
- `DBInsert`
- `DBKeyedInsert`
- `NewDB`
- `Instance`
- `PackGet`
- `TryPackGet`
- `UnpackGet`
- `PackGetNamedStatParams`
- `TryPackGetNamedStatParams`
- `UnpackGetNamedStatParams`
- `PackGetStatParams`
- `TryPackGetStatParams`
- `UnpackGetStatParams`
- `PackGetStatsStruct`
- `TryPackGetStatsStruct`
- `UnpackGetStatsStruct`
- `PackInsert`
- `TryPackInsert`
- `UnpackInsert`
- `ContractEventName`
- `UnpackInsertEvent`
- `ContractEventName`
- `UnpackKeyedInsertEvent`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Code generated via abigen V2 - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package db

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