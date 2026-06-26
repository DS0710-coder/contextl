# sync_test.go

## Architecture Metrics
- **Path:** `core/state/sync_test.go`
- **Extension:** `.go`
- **Size:** 25792 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testAccount`
- `stateElement`
- `makeTestState`
- `checkStateAccounts`
- `checkStateConsistency`
- `TestEmptyStateSync`
- `TestIterativeStateSyncIndividual`
- `TestIterativeStateSyncBatched`
- `TestIterativeStateSyncIndividualFromDisk`
- `TestIterativeStateSyncBatchedFromDisk`
- `TestIterativeStateSyncIndividualByPath`
- `TestIterativeStateSyncBatchedByPath`
- `testIterativeStateSync`
- `TestIterativeDelayedStateSync`
- `testIterativeDelayedStateSync`
- `TestIterativeRandomStateSyncIndividual`
- `TestIterativeRandomStateSyncBatched`
- `testIterativeRandomStateSync`
- `TestIterativeRandomDelayedStateSync`
- `testIterativeRandomDelayedStateSync`
- `TestIncompleteStateSync`
- `testIncompleteStateSync`
- `copyPreimages`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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
	"bytes"
...
```