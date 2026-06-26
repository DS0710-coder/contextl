# iterator.go

## Architecture Metrics
- **Path:** `trie/iterator.go`
- **Extension:** `.go`
- **Size:** 27890 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Iterator`
- `NodeIterator`
- `nodeIteratorState`
- `nodeIterator`
- `seekError`
- `differenceIterator`
- `unionIterator`
- `subtreeIterator`
- `NewIterator`
- `Next`
- `Prove`
- `Error`
- `newNodeIterator`
- `putInPool`
- `getFromPool`
- `AddResolver`
- `Hash`
- `Parent`
- `Leaf`
- `LeafKey`
- `LeafBlob`
- `LeafProof`
- `Path`
- `NodeBlob`
- `Error`
- `Next`
- `seek`
- `init`
- `peek`
- `peekSeek`
- `resolveHash`
- `resolveBlob`
- `resolve`
- `findChild`
- `nextChild`
- `nextChildAt`
- `push`
- `pop`
- `reachedPath`
- `prevChildIndex`
- `nextChildIndex`
- `compareNodes`
- `NewDifferenceIterator`
- `Hash`
- `Parent`
- `Leaf`
- `LeafKey`
- `LeafBlob`
- `LeafProof`
- `Path`
- `NodeBlob`
- `AddResolver`
- `Next`
- `Error`
- `Len`
- `Less`
- `Swap`
- `Push`
- `Pop`
- `NewUnionIterator`
- `Hash`
- `Parent`
- `Leaf`
- `LeafKey`
- `LeafBlob`
- `LeafProof`
- `Path`
- `NodeBlob`
- `AddResolver`
- `Next`
- `Error`
- `newSubtreeIterator`
- `nextKey`
- `newPrefixIterator`
- `Next`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

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

package trie

import (
	"bytes"
...
```