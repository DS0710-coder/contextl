# memorydb.go

## Architecture Metrics
- **Path:** `ethdb/memorydb/memorydb.go`
- **Extension:** `.go`
- **Size:** 10764 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 13
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Database`
- `keyvalue`
- `batch`
- `iterator`
- `New`
- `NewWithCap`
- `Close`
- `Has`
- `Get`
- `Put`
- `Delete`
- `DeleteRange`
- `NewBatch`
- `NewBatchWithSize`
- `NewIterator`
- `Stat`
- `Compact`
- `SyncKeyValue`
- `Len`
- `Put`
- `Delete`
- `DeleteRange`
- `ValueSize`
- `Write`
- `Reset`
- `Replay`
- `Close`
- `Next`
- `Error`
- `Key`
- `Value`
- `Release`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]

## Imported By (Dependents)
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/light/committee_chain_test.go.md|beacon/light/committee_chain_test.go]]
- [[core/rawdb/database.go.md|core/rawdb/database.go]]
- [[core/state/snapshot/context.go.md|core/state/snapshot/context.go]]
- [[core/state/snapshot/difflayer_test.go.md|core/state/snapshot/difflayer_test.go]]
- [[core/state/snapshot/disklayer_test.go.md|core/state/snapshot/disklayer_test.go]]
- [[node/node.go.md|node/node.go]]
- [[tests/fuzzers/rangeproof/rangeproof-fuzzer.go.md|tests/fuzzers/rangeproof/rangeproof-fuzzer.go]]
- [[trie/proof_test.go.md|trie/proof_test.go]]
- [[trie/sync_test.go.md|trie/sync_test.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/internal/holdable_iterator_test.go.md|triedb/internal/holdable_iterator_test.go]]
- [[triedb/pathdb/context.go.md|triedb/pathdb/context.go]]

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

// Package memorydb implements the key-value database layer based on memory maps.
package memorydb

import (
...
```