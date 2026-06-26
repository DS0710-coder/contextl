# generate_test.go

## Architecture Metrics
- **Path:** `triedb/generate_test.go`
- **Extension:** `.go`
- **Size:** 22821 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testAccount`
- `testSlot`
- `peakBatch`
- `peakBatchDB`
- `buildExpectedRoot`
- `computeStorageRootFromSlots`
- `TestGenerateTrieEmpty`
- `TestGenerateTrieAccountsOnly`
- `TestGenerateTrieWithStorage`
- `TestGenerateTrieRootMismatch`
- `TestGenerateTrieFixesStaleRoots`
- `TestGenerateTrieCancel`
- `TestGenerateTrieOrphanStorage`
- `TestHashRanges`
- `TestGenerateTriePathSchemeNodeSet`
- `assertCanonicalNodes`
- `diskNodeKeys`
- `assertSameNodeSet`
- `Write`
- `NewBatch`
- `NewBatchWithSize`
- `TestGenerateTrieBatchFlush`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package triedb

import (
	"bytes"
...
```