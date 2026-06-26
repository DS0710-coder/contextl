# buffer.go

## Architecture Metrics
- **Path:** `triedb/pathdb/buffer.go`
- **Extension:** `.go`
- **Size:** 7220 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 20
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `buffer`
- `newBuffer`
- `account`
- `storage`
- `node`
- `commit`
- `revertTo`
- `reset`
- `empty`
- `full`
- `size`
- `flush`
- `waitFlush`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]

## Imported By (Dependents)
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/genesis_test.go.md|core/genesis_test.go]]
- [[core/state/database_history.go.md|core/state/database_history.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/state_sizer_test.go.md|core/state/state_sizer_test.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/history.go.md|triedb/history.go]]
- [[triedb/states.go.md|triedb/states.go]]

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package pathdb

import (
	"errors"
...
```