# store_commit.go

## Architecture Metrics
- **Path:** `trie/bintrie/store_commit.go`
- **Extension:** `.go`
- **Size:** 18062 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Hash`
- `computeHash`
- `hashInternal`
- `serializeSubtree`
- `packedDepthsLen`
- `writeDepth`
- `readDepth`
- `serializeNode`
- `deserializeNode`
- `deserializeNodeWithHash`
- `deserializeSubtree`
- `attachInGroup`
- `decodeNode`
- `collectNodes`
- `collectChildGroups`
- `toDot`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 go-ethereum Authors
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

package bintrie

import (
	"crypto/sha256"
...
```