# goja.go

## Architecture Metrics
- **Path:** `eth/tracers/js/goja.go`
- **Extension:** `.go`
- **Size:** 27146 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `jsTracer`
- `opObj`
- `memoryObj`
- `stackObj`
- `dbObj`
- `contractObj`
- `callframe`
- `callframeResult`
- `steplog`
- `init`
- `getBigIntProgram`
- `toBuf`
- `fromBuf`
- `newJsTracer`
- `OnTxStart`
- `OnTxEnd`
- `onStart`
- `OnOpcode`
- `OnFault`
- `onEnd`
- `OnEnter`
- `OnExit`
- `GetResult`
- `Stop`
- `onError`
- `wrapError`
- `setBuiltinFunctions`
- `setTypeConverters`
- `ToNumber`
- `ToString`
- `IsPush`
- `setupObject`
- `Slice`
- `slice`
- `GetUint`
- `getUint`
- `Length`
- `setupObject`
- `Peek`
- `peek`
- `Length`
- `setupObject`
- `GetBalance`
- `GetNonce`
- `GetCode`
- `GetState`
- `Exists`
- `setupObject`
- `GetCaller`
- `GetAddress`
- `GetValue`
- `GetInput`
- `setupObject`
- `GetType`
- `GetFrom`
- `GetTo`
- `GetInput`
- `GetGas`
- `GetValue`
- `setupObject`
- `GetGasUsed`
- `GetOutput`
- `GetError`
- `setupObject`
- `GetPC`
- `GetGas`
- `GetCost`
- `GetDepth`
- `GetRefund`
- `GetError`
- `setupObject`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/internal/util.go.md|eth/tracers/internal/util.go]]
- [[eth/tracers/js/internal/tracers/tracers.go.md|eth/tracers/js/internal/tracers/tracers.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package js

import (
	"encoding/json"
...
```