# gen_balance_change_reason_stringer.go

## Architecture Metrics
- **Path:** `core/tracing/gen_balance_change_reason_stringer.go`
- **Extension:** `.go`
- **Size:** 1793 bytes
- **Centrality Score:** 0.0032
- **In-Degree (Imported By):** 69
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `_`
- `String`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/file_tracer.go.md|cmd/evm/internal/t8ntool/file_tracer.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[consensus/misc/dao.go.md|consensus/misc/dao.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/evm.go.md|core/evm.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/state/journal_test.go.md|core/state/journal_test.go]]
- [[core/state/state_sizer_test.go.md|core/state/state_sizer_test.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_hooked.go.md|core/state/statedb_hooked.go]]
- [[core/state/statedb_hooked_test.go.md|core/state/statedb_hooked_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/stateupdate.go.md|core/state/stateupdate.go]]
- [[core/state/trie_prefetcher_test.go.md|core/state/trie_prefetcher_test.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/state_transition.go.md|core/state_transition.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/cache_test.go.md|core/txpool/blobpool/cache_test.go]]
- [[core/txpool/legacypool/legacypool2_test.go.md|core/txpool/legacypool/legacypool2_test.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/vm/contract.go.md|core/vm/contract.go]]
- [[core/vm/contracts.go.md|core/vm/contracts.go]]
- [[core/vm/eip8037_test.go.md|core/vm/eip8037_test.go]]
- [[core/vm/eips.go.md|core/vm/eips.go]]
- [[core/vm/evm.go.md|core/vm/evm.go]]
- [[core/vm/gas_table_test.go.md|core/vm/gas_table_test.go]]
- [[core/vm/gascosts.go.md|core/vm/gascosts.go]]
- [[core/vm/instructions.go.md|core/vm/instructions.go]]
- [[core/vm/interface.go.md|core/vm/interface.go]]
- [[core/vm/interpreter.go.md|core/vm/interpreter.go]]
- [[core/vm/interpreter_test.go.md|core/vm/interpreter_test.go]]
- [[core/vm/operations_acl.go.md|core/vm/operations_acl.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/dir.go.md|eth/tracers/dir.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/js/goja.go.md|eth/tracers/js/goja.go]]
- [[eth/tracers/live.go.md|eth/tracers/live.go]]
- [[eth/tracers/live/noop.go.md|eth/tracers/live/noop.go]]
- [[eth/tracers/live/supply.go.md|eth/tracers/live/supply.go]]
- [[eth/tracers/logger/access_list_tracer.go.md|eth/tracers/logger/access_list_tracer.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[eth/tracers/logger/logger_json.go.md|eth/tracers/logger/logger_json.go]]
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
- [[internal/ethapi/logtracer.go.md|internal/ethapi/logtracer.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]

## Source Code Snippet
```go
// Code generated by "stringer -type=BalanceChangeReason -trimprefix=BalanceChange -output gen_balance_change_reason_stringer.go"; DO NOT EDIT.

package tracing

import "strconv"

func _() {
	// An "invalid array index" compiler error signifies that the constant values have changed.
	// Re-run the stringer command to generate them again.
	var x [1]struct{}
	_ = x[BalanceChangeUnspecified-0]
	_ = x[BalanceIncreaseRewardMineUncle-1]
	_ = x[BalanceIncreaseRewardMineBlock-2]
	_ = x[BalanceIncreaseWithdrawal-3]
	_ = x[BalanceIncreaseGenesisBalance-4]
	_ = x[BalanceIncreaseRewardTransactionFee-5]
	_ = x[BalanceDecreaseGasBuy-6]
	_ = x[BalanceIncreaseGasReturn-7]
	_ = x[BalanceIncreaseDaoContract-8]
	_ = x[BalanceDecreaseDaoAccount-9]
...
```