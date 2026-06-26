# ethash.go

## Architecture Metrics
- **Path:** `consensus/ethash/ethash.go`
- **Extension:** `.go`
- **Size:** 2940 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 48
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Ethash`
- `NewFaker`
- `NewFakeFailer`
- `NewFakeDelayer`
- `NewFullFaker`
- `Close`
- `Seal`

## Imports (Dependencies)
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/types.go.md|core/types.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/block_validator_test.go.md|core/block_validator_test.go]]
- [[core/blockchain_repair_test.go.md|core/blockchain_repair_test.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/blockchain_snapshot_test.go.md|core/blockchain_snapshot_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers_test.go.md|core/chain_makers_test.go]]
- [[core/dao_test.go.md|core/dao_test.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/eth_transfer_logs_test.go.md|core/eth_transfer_logs_test.go]]
- [[core/filtermaps/indexer_test.go.md|core/filtermaps/indexer_test.go]]
- [[core/genesis_test.go.md|core/genesis_test.go]]
- [[core/headerchain_test.go.md|core/headerchain_test.go]]
- [[core/rlp_test.go.md|core/rlp_test.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/txindexer_test.go.md|core/txindexer_test.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/queue_test.go.md|eth/downloader/queue_test.go]]
- [[eth/downloader/testchain_test.go.md|eth/downloader/testchain_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/snap/handler_fuzzing_test.go.md|eth/protocols/snap/handler_fuzzing_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/difficulty_test_util.go.md|tests/difficulty_test_util.go]]
- [[tests/fuzzers/difficulty/difficulty-fuzz.go.md|tests/fuzzers/difficulty/difficulty-fuzz.go]]

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

// Package ethash implements the ethash proof-of-work consensus engine.
package ethash

import (
...
```