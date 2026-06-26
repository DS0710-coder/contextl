# logger.go

## Architecture Metrics
- **Path:** `eth/tracers/logger/logger.go`
- **Extension:** `.go`
- **Size:** 16269 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `StructLog`
- `structLogMarshaling`
- `structLogLegacy`
- `StructLogger`
- `mdLogger`
- `ExecutionResult`
- `OpName`
- `ErrorString`
- `Write`
- `formatMemoryWord`
- `toLegacyJSON`
- `NewStreamingStructLogger`
- `NewStructLogger`
- `Hooks`
- `OnOpcode`
- `OnExit`
- `GetResult`
- `Stop`
- `OnTxStart`
- `OnSystemCallStart`
- `OnSystemCallEnd`
- `OnTxEnd`
- `Error`
- `Output`
- `WriteTrace`
- `NewMarkdownLogger`
- `Hooks`
- `OnTxStart`
- `OnSystemCallStart`
- `OnSystemCallEnd`
- `OnEnter`
- `OnExit`
- `OnOpcode`
- `OnFault`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/workload/tracetestgen.go.md|cmd/workload/tracetestgen.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/tracers_test.go.md|eth/tracers/tracers_test.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[tests/state_test.go.md|tests/state_test.go]]

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

package logger

import (
	"encoding/hex"
...
```