# database.go

## Architecture Metrics
- **Path:** `triedb/hashdb/database.go`
- **Extension:** `.go`
- **Size:** 23373 bytes
- **Centrality Score:** 0.0007
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `Database`
- `cachedNode`
- `cleaner`
- `reader`
- `forChildren`
- `New`
- `insert`
- `node`
- `Reference`
- `reference`
- `Dereference`
- `dereference`
- `Cap`
- `Commit`
- `commit`
- `Put`
- `Delete`
- `Update`
- `Size`
- `Close`
- `NodeReader`
- `Node`
- `StateReader`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/preimages_test.go.md|triedb/preimages_test.go]]

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

package hashdb

import (
	"errors"
...
```