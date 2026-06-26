# state_object.go

## Architecture Metrics
- **Path:** `core/state/state_object.go`
- **Extension:** `.go`
- **Size:** 22134 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `stateObject`
- `Copy`
- `empty`
- `newObject`
- `addrHash`
- `markSelfdestructed`
- `touch`
- `getTrie`
- `getPrefetchedTrie`
- `GetState`
- `getState`
- `GetCommittedState`
- `SetState`
- `setState`
- `finalise`
- `updateTrie`
- `updateRoot`
- `commitStorage`
- `commit`
- `AddBalance`
- `SetBalance`
- `setBalance`
- `deepCopy`
- `Address`
- `Code`
- `CodeSize`
- `SetCode`
- `setCode`
- `SetNonce`
- `setNonce`
- `CodeHash`
- `Balance`
- `Nonce`
- `Root`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[trie/bintrie/binary_node.go.md|trie/bintrie/binary_node.go]]
- [[trie/bytepool.go.md|trie/bytepool.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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