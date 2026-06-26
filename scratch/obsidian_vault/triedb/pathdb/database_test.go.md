# database_test.go

## Architecture Metrics
- **Path:** `triedb/pathdb/database_test.go`
- **Extension:** `.go`
- **Size:** 32945 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `genctx`
- `tester`
- `testerConfig`
- `updateTrie`
- `generateAccount`
- `newCtx`
- `storageOriginSet`
- `trieCacheSize`
- `stateCacheSize`
- `writeBufferSize`
- `newTester`
- `accountPreimage`
- `hashPreimage`
- `extend`
- `release`
- `randAccount`
- `generateStorage`
- `mutateStorage`
- `clearStorage`
- `resurrectStorage`
- `generate`
- `lastHash`
- `verifyState`
- `verifyHistory`
- `bottomIndex`
- `TestDatabaseRollback`
- `TestDatabaseRecoverable`
- `TestExecuteRollback`
- `TestDisable`
- `TestAdoptSyncedState`
- `TestCommit`
- `TestJournal`
- `testJournal`
- `TestCorruptedJournal`
- `testCorruptedJournal`
- `TestTailTruncateHistory`
- `copyAccounts`
- `copyStorages`
- `TestDatabaseIndexRecovery`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/testrand/rand.go.md|internal/testrand/rand.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

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
	"bytes"
...
```