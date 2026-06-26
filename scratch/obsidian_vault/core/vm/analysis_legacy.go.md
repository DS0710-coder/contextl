# analysis_legacy.go

## Architecture Metrics
- **Path:** `core/vm/analysis_legacy.go`
- **Extension:** `.go`
- **Size:** 3183 bytes
- **Centrality Score:** 0.0104
- **In-Degree (Imported By):** 85
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `set1`
- `setN`
- `set8`
- `set16`
- `codeSegment`
- `codeBitmap`
- `codeBitmapInternal`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/flags.go.md|cmd/evm/internal/t8ntool/flags.go]]
- [[cmd/evm/internal/t8ntool/transaction.go.md|cmd/evm/internal/t8ntool/transaction.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/evm/staterunner.go.md|cmd/evm/staterunner.go]]
- [[cmd/keeper/main.go.md|cmd/keeper/main.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[consensus/misc/dao.go.md|consensus/misc/dao.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/evm.go.md|core/evm.go]]
- [[core/jumpdest.go.md|core/jumpdest.go]]
- [[core/state_prefetcher.go.md|core/state_prefetcher.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/state_transition.go.md|core/state_transition.go]]
- [[core/state_transition_test.go.md|core/state_transition_test.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/validation.go.md|core/txpool/validation.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/program/program.go.md|core/vm/program/program.go]]
- [[core/vm/program/program_test.go.md|core/vm/program/program_test.go]]
- [[core/vm/runtime/env.go.md|core/vm/runtime/env.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[eth/gasestimator/gasestimator.go.md|eth/gasestimator/gasestimator.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[eth/tracers/internal/tracetest/prestate_test.go.md|eth/tracers/internal/tracetest/prestate_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/internal/tracetest/util.go.md|eth/tracers/internal/tracetest/util.go]]
- [[eth/tracers/internal/util_test.go.md|eth/tracers/internal/util_test.go]]
- [[eth/tracers/js/goja.go.md|eth/tracers/js/goja.go]]
- [[eth/tracers/js/tracer_test.go.md|eth/tracers/js/tracer_test.go]]
- [[eth/tracers/live/supply.go.md|eth/tracers/live/supply.go]]
- [[eth/tracers/logger/access_list_tracer.go.md|eth/tracers/logger/access_list_tracer.go]]
- [[eth/tracers/logger/gen_structlog.go.md|eth/tracers/logger/gen_structlog.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[eth/tracers/logger/logger_json.go.md|eth/tracers/logger/logger_json.go]]
- [[eth/tracers/logger/logger_test.go.md|eth/tracers/logger/logger_test.go]]
- [[eth/tracers/native/4byte.go.md|eth/tracers/native/4byte.go]]
- [[eth/tracers/native/call.go.md|eth/tracers/native/call.go]]
- [[eth/tracers/native/call_flat.go.md|eth/tracers/native/call_flat.go]]
- [[eth/tracers/native/call_flat_test.go.md|eth/tracers/native/call_flat_test.go]]
- [[eth/tracers/native/erc7562.go.md|eth/tracers/native/erc7562.go]]
- [[eth/tracers/native/gen_callframe_json.go.md|eth/tracers/native/gen_callframe_json.go]]
- [[eth/tracers/native/gen_callframewithopcodes_json.go.md|eth/tracers/native/gen_callframewithopcodes_json.go]]
- [[eth/tracers/native/keccak256_preimage.go.md|eth/tracers/native/keccak256_preimage.go]]
- [[eth/tracers/native/keccak256_preimage_test.go.md|eth/tracers/native/keccak256_preimage_test.go]]
- [[eth/tracers/native/opcode_counter.go.md|eth/tracers/native/opcode_counter.go]]
- [[eth/tracers/native/prestate.go.md|eth/tracers/native/prestate.go]]
- [[eth/tracers/native/tracer_test.go.md|eth/tracers/native/tracer_test.go]]
- [[eth/tracers/tracers_test.go.md|eth/tracers/tracers_test.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/errors.go.md|internal/ethapi/errors.go]]
- [[internal/ethapi/logtracer.go.md|internal/ethapi/logtracer.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[internal/ethapi/override/override_test.go.md|internal/ethapi/override/override_test.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/worker.go.md|miner/worker.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/fuzzers/bls12381/precompile_fuzzer.go.md|tests/fuzzers/bls12381/precompile_fuzzer.go]]
- [[tests/state_test.go.md|tests/state_test.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]

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

const (
	set2BitsMask = uint16(0b11)
...
```