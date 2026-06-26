# binary_node.go

## Architecture Metrics
- **Path:** `trie/bintrie/binary_node.go`
- **Extension:** `.go`
- **Size:** 2056 bytes
- **Centrality Score:** 0.0024
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bitmapSizeForDepth`
- `DeserializeAndHash`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/database_ubt.go.md|core/state/database_ubt.go]]
- [[core/state/dump.go.md|core/state/dump.go]]
- [[core/state/reader.go.md|core/state/reader.go]]
- [[core/state/state_object.go.md|core/state/state_object.go]]
- [[trie/transitiontrie/transition.go.md|trie/transitiontrie/transition.go]]
- [[triedb/pathdb/database.go.md|triedb/pathdb/database.go]]

## Source Code Snippet
```go
// Copyright 2025 go-ethereum Authors
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

import "github.com/ethereum/go-ethereum/common"

...
```