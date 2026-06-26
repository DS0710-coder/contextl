# bintrie_convert.go

## Architecture Metrics
- **Path:** `cmd/geth/bintrie_convert.go`
- **Extension:** `.go`
- **Size:** 12773 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 15

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `conversionStats`
- `report`
- `convertToBinaryTrie`
- `runConversionLoop`
- `maybeCommit`
- `commitBinaryTrie`
- `deleteMPTData`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/bintrie/binary_node.go.md|trie/bintrie/binary_node.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package main

import (
	"errors"
...
```