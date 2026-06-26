# evm.go

## Architecture Metrics
- **Path:** `core/vm/evm.go`
- **Extension:** `.go`
- **Size:** 29866 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockContext`
- `TxContext`
- `EVM`
- `precompile`
- `NewEVM`
- `SetPrecompiles`
- `SetJumpDestCache`
- `SetTxContext`
- `Cancel`
- `Release`
- `Cancelled`
- `isSystemCall`
- `Call`
- `CallCode`
- `DelegateCall`
- `StaticCall`
- `create`
- `initNewContract`
- `Create`
- `Create2`
- `resolveCode`
- `resolveCodeHash`
- `ChainConfig`
- `captureBegin`
- `captureEnd`
- `GetVMContext`
- `GetRules`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
// This file is part of the go-ethereum library.
//
// The go-ethereum library is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// The go-ethereum library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with the go-ethereum library. If not, see <http://www.gnu.org/licenses/>.

package vm

import (
	"errors"
...
```