# reader.go

## Architecture Metrics
- **Path:** `core/state/reader.go`
- **Extension:** `.go`
- **Size:** 20120 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ContractCodeReader`
- `StateReader`
- `Reader`
- `flatReader`
- `mptTrieReader`
- `ubtTrieReader`
- `multiStateReader`
- `stateReaderWithCache`
- `stateReaderWithStats`
- `reader`
- `newFlatReader`
- `Account`
- `Storage`
- `newMPTTrieReader`
- `account`
- `Account`
- `Storage`
- `newUBTTrieReader`
- `Account`
- `Storage`
- `newMultiStateReader`
- `Account`
- `Storage`
- `newStateReaderWithCache`
- `account`
- `Account`
- `storage`
- `Storage`
- `newStateReaderWithStats`
- `Account`
- `Storage`
- `GetStateStats`
- `newReader`
- `GetCodeStats`
- `GetStateStats`
- `GetStats`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/overlay/state_transition.go.md|core/overlay/state_transition.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/bintrie/binary_node.go.md|trie/bintrie/binary_node.go]]
- [[trie/bytepool.go.md|trie/bytepool.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package state

import (
	"errors"
...
```