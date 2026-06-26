# consensus.go

## Architecture Metrics
- **Path:** `consensus/beacon/consensus.go`
- **Extension:** `.go`
- **Size:** 16634 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 23
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Beacon`
- `threaded`
- `New`
- `Author`
- `VerifyHeader`
- `splitHeaders`
- `VerifyHeaders`
- `VerifyUncles`
- `verifyHeader`
- `verifyHeaders`
- `Prepare`
- `Finalize`
- `Seal`
- `SealHash`
- `CalcDifficulty`
- `Close`
- `IsPoSHeader`
- `InnerEngine`
- `SetThreads`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/block_validator_test.go.md|core/block_validator_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers_test.go.md|core/chain_makers_test.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/eth_transfer_logs_test.go.md|core/eth_transfer_logs_test.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]

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

package beacon

import (
	"errors"
...
```