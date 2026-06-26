# bal.go

## Architecture Metrics
- **Path:** `core/types/bal/bal.go`
- **Extension:** `.go`
- **Size:** 8294 bytes
- **Centrality Score:** 0.0087
- **In-Degree (Imported By):** 29
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConstructionAccountAccess`
- `ConstructionBlockAccessList`
- `NewConstructionAccountAccess`
- `NewConstructionBlockAccessList`
- `AccountRead`
- `StorageRead`
- `StorageWrite`
- `CodeChange`
- `NonceChange`
- `BalanceChange`
- `PrettyPrint`
- `Merge`
- `Copy`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]

## Imported By (Dependents)
- [[beacon/engine/ed_codec.go.md|beacon/engine/ed_codec.go]]
- [[beacon/engine/types.go.md|beacon/engine/types.go]]
- [[cmd/devp2p/internal/ethtest/snap2.go.md|cmd/devp2p/internal/ethtest/snap2.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/rawdb/accessors_chain_test.go.md|core/rawdb/accessors_chain_test.go]]
- [[core/state/reader_eip_7928.go.md|core/state/reader_eip_7928.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_hooked.go.md|core/state/statedb_hooked.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/block.go.md|core/types/block.go]]
- [[core/vm/interface.go.md|core/vm/interface.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/protocol.go.md|eth/protocols/eth/protocol.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/protocols/snap/bal_apply_test.go.md|eth/protocols/snap/bal_apply_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[miner/worker.go.md|miner/worker.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

package bal

import (
	"bytes"
...
```