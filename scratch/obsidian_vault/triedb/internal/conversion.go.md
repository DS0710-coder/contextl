# conversion.go

## Architecture Metrics
- **Path:** `triedb/internal/conversion.go`
- **Extension:** `.go`
- **Size:** 12222 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Iterator`
- `AccountIterator`
- `StorageIterator`
- `TrieKV`
- `GenerateStats`
- `NewGenerateStats`
- `ProgressAccounts`
- `FinishAccounts`
- `ProgressContract`
- `FinishContract`
- `Report`
- `ReportDone`
- `RunReport`
- `GenerateTrieRoot`
- `StackTrieGenerate`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/pathdb/context.go.md|triedb/pathdb/context.go]]
- [[triedb/pathdb/iterator.go.md|triedb/pathdb/iterator.go]]
- [[triedb/pathdb/verifier.go.md|triedb/pathdb/verifier.go]]

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

// Package internal contains shared trie generation utilities used by both
// triedb and triedb/pathdb. All code is ported from
// core/state/snapshot/conversion.go (with exported names) unless noted.
package internal
...
```