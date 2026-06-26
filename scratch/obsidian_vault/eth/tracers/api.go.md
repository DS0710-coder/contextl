# api.go

## Architecture Metrics
- **Path:** `eth/tracers/api.go`
- **Extension:** `.go`
- **Size:** 40260 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 34
- **Out-Degree (Imports):** 18

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Backend`
- `API`
- `TraceConfig`
- `TraceCallConfig`
- `StdTraceConfig`
- `txTraceResult`
- `blockTraceTask`
- `blockTraceResult`
- `txTraceTask`
- `NewAPI`
- `chainContext`
- `blockByNumber`
- `blockByHash`
- `blockByNumberAndHash`
- `TraceChain`
- `traceChain`
- `TraceBlockByNumber`
- `TraceBlockByHash`
- `TraceBlock`
- `TraceBlockFromFile`
- `TraceBadBlock`
- `StandardTraceBlockToFile`
- `IntermediateRoots`
- `StandardTraceBadBlockToFile`
- `traceBlock`
- `traceBlockParallel`
- `standardTraceBlockToFile`
- `containsTx`
- `TraceTransaction`
- `TraceCall`
- `traceTx`
- `APIs`
- `overrideConfig`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/file_tracer.go.md|cmd/evm/internal/t8ntool/file_tracer.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/workload/prooftestgen.go.md|cmd/workload/prooftestgen.go]]
- [[cmd/workload/tracetest.go.md|cmd/workload/tracetest.go]]
- [[cmd/workload/tracetestgen.go.md|cmd/workload/tracetestgen.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[eth/tracers/internal/tracetest/prestate_test.go.md|eth/tracers/internal/tracetest/prestate_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/js/goja.go.md|eth/tracers/js/goja.go]]
- [[eth/tracers/js/tracer_test.go.md|eth/tracers/js/tracer_test.go]]
- [[eth/tracers/live/noop.go.md|eth/tracers/live/noop.go]]
- [[eth/tracers/live/supply.go.md|eth/tracers/live/supply.go]]
- [[eth/tracers/native/4byte.go.md|eth/tracers/native/4byte.go]]
- [[eth/tracers/native/call.go.md|eth/tracers/native/call.go]]
- [[eth/tracers/native/call_flat.go.md|eth/tracers/native/call_flat.go]]
- [[eth/tracers/native/call_flat_test.go.md|eth/tracers/native/call_flat_test.go]]
- [[eth/tracers/native/erc7562.go.md|eth/tracers/native/erc7562.go]]
- [[eth/tracers/native/keccak256_preimage.go.md|eth/tracers/native/keccak256_preimage.go]]
- [[eth/tracers/native/keccak256_preimage_test.go.md|eth/tracers/native/keccak256_preimage_test.go]]
- [[eth/tracers/native/mux.go.md|eth/tracers/native/mux.go]]
- [[eth/tracers/native/mux_test.go.md|eth/tracers/native/mux_test.go]]
- [[eth/tracers/native/noop.go.md|eth/tracers/native/noop.go]]
- [[eth/tracers/native/opcode_counter.go.md|eth/tracers/native/opcode_counter.go]]
- [[eth/tracers/native/prestate.go.md|eth/tracers/native/prestate.go]]
- [[eth/tracers/native/tracer_test.go.md|eth/tracers/native/tracer_test.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
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

package tracers

import (
	"bufio"
...
```