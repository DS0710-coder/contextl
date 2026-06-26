# consensus.go

## Architecture Metrics
- **Path:** `consensus/consensus.go`
- **Extension:** `.go`
- **Size:** 4661 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 32
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChainHeaderReader`
- `ChainReader`
- `Engine`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/block_validator.go.md|core/block_validator.go]]
- [[core/block_validator_test.go.md|core/block_validator_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/blockchain_snapshot_test.go.md|core/blockchain_snapshot_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/evm.go.md|core/evm.go]]
- [[core/headerchain.go.md|core/headerchain.go]]
- [[core/headerchain_test.go.md|core/headerchain_test.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]

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

// Package consensus implements different Ethereum consensus engines.
package consensus

import (
...
```