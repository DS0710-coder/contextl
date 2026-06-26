# 4byte.go

## Architecture Metrics
- **Path:** `eth/tracers/native/4byte.go`
- **Extension:** `.go`
- **Size:** 4667 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `fourByteTracer`
- `init`
- `newFourByteTracer`
- `isPrecompiled`
- `store`
- `OnTxStart`
- `OnEnter`
- `GetResult`
- `Stop`
- `bytesToHex`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/workload/prooftestgen.go.md|cmd/workload/prooftestgen.go]]
- [[eth/tracers/internal/tracetest/util.go.md|eth/tracers/internal/tracetest/util.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]

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