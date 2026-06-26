# runtime_test.go

## Architecture Metrics
- **Path:** `core/vm/runtime/runtime_test.go`
- **Extension:** `.go`
- **Size:** 34333 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `dummyChain`
- `TestDefaults`
- `TestDefaultsPreserveRandom`
- `TestEVM`
- `TestExecute`
- `TestCall`
- `BenchmarkCall`
- `benchmarkEVM_Create`
- `BenchmarkEVM_CREATE_500`
- `BenchmarkEVM_CREATE2_500`
- `BenchmarkEVM_CREATE_1200`
- `BenchmarkEVM_CREATE2_1200`
- `BenchmarkEVM_SWAP1`
- `BenchmarkEVM_RETURN`
- `fakeHeader`
- `Engine`
- `GetHeader`
- `Config`
- `CurrentHeader`
- `GetHeaderByNumber`
- `GetHeaderByHash`
- `TestBlockhash`
- `benchmarkNonModifyingCode`
- `BenchmarkSimpleLoop`
- `TestEip2929Cases`
- `TestColdAccountAccessCost`
- `TestRuntimeJSTracer`
- `TestJSTracerCreateTx`
- `BenchmarkTracerStepVsCallFrame`
- `TestDelegatedAccountAccessCost`
- `TestManyLargeStacks`
- `BenchmarkLargeDeepStacks`
- `BenchmarkShortDeepStacks`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[core/vm/program/program.go.md|core/vm/program/program.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/js/bigint.go.md|eth/tracers/js/bigint.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package runtime

import (
	"encoding/binary"
...
```