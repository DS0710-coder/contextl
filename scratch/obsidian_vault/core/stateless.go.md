# stateless.go

## Architecture Metrics
- **Path:** `core/stateless.go`
- **Extension:** `.go`
- **Size:** 3820 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 12
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ExecuteStateless`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
- [[cmd/fetchpayload/main.go.md|cmd/fetchpayload/main.go]]
- [[cmd/keeper/getpayload_example.go.md|cmd/keeper/getpayload_example.go]]
- [[cmd/keeper/main.go.md|cmd/keeper/main.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_hooked.go.md|core/state/statedb_hooked.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/vm/interface.go.md|core/vm/interface.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[miner/payload_building.go.md|miner/payload_building.go]]
- [[miner/worker.go.md|miner/worker.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package core

import (
	"context"
...
```