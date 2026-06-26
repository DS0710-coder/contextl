# access_events.go

## Architecture Metrics
- **Path:** `core/state/access_events.go`
- **Extension:** `.go`
- **Size:** 12355 bytes
- **Centrality Score:** 0.0090
- **In-Degree (Imported By):** 71
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AccessEvents`
- `branchAccessKey`
- `chunkAccessKey`
- `NewAccessEvents`
- `Merge`
- `Keys`
- `Copy`
- `AddAccount`
- `MessageCallGas`
- `ValueTransferGas`
- `ContractCreatePreCheckGas`
- `ContractCreateInitGas`
- `AddTxOrigin`
- `AddTxDestination`
- `SlotGas`
- `touchAddressAndChargeGas`
- `newBranchAccessKey`
- `newChunkAccessKey`
- `CodeChunksRangeGas`
- `BasicDataGas`
- `CodeHashGas`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/bintrie/binary_node.go.md|trie/bintrie/binary_node.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/evm/reporter.go.md|cmd/evm/reporter.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/block_validator.go.md|core/block_validator.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/blockchain_stats.go.md|core/blockchain_stats.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/state_prefetcher.go.md|core/state_prefetcher.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/cache_test.go.md|core/txpool/blobpool/cache_test.go]]
- [[core/txpool/blobpool/interface.go.md|core/txpool/blobpool/interface.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/legacypool/legacypool2_test.go.md|core/txpool/legacypool/legacypool2_test.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/legacypool/noncer.go.md|core/txpool/legacypool/noncer.go]]
- [[core/txpool/legacypool/queue.go.md|core/txpool/legacypool/queue.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/txpool/validation.go.md|core/txpool/validation.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/eip8037_test.go.md|core/vm/eip8037_test.go]]
- [[core/vm/evm.go.md|core/vm/evm.go]]
- [[core/vm/gas_table_test.go.md|core/vm/gas_table_test.go]]
- [[core/vm/instructions_test.go.md|core/vm/instructions_test.go]]
- [[core/vm/interface.go.md|core/vm/interface.go]]
- [[core/vm/interpreter_test.go.md|core/vm/interpreter_test.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/gasestimator/gasestimator.go.md|eth/gasestimator/gasestimator.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/js/tracer_test.go.md|eth/tracers/js/tracer_test.go]]
- [[eth/tracers/logger/logger_test.go.md|eth/tracers/logger/logger_test.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/capabilities.go.md|internal/ethapi/capabilities.go]]
- [[internal/ethapi/capabilities_test.go.md|internal/ethapi/capabilities_test.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[internal/ethapi/override/override_test.go.md|internal/ethapi/override/override_test.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/worker.go.md|miner/worker.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]

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

package state

import (
	"maps"
...
```