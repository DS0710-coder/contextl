# noop.go

## Architecture Metrics
- **Path:** `eth/tracers/native/noop.go`
- **Extension:** `.go`
- **Size:** 3594 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `noopTracer`
- `init`
- `newNoopTracer`
- `OnOpcode`
- `OnFault`
- `OnGasChange`
- `OnGasChangeV2`
- `OnEnter`
- `OnExit`
- `OnTxStart`
- `OnTxEnd`
- `OnBalanceChange`
- `OnNonceChange`
- `OnCodeChange`
- `OnStorageChange`
- `OnLog`
- `GetResult`
- `Stop`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package native

import (
	"encoding/json"
...
```