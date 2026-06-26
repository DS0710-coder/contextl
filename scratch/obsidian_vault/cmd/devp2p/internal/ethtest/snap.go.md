# snap.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/ethtest/snap.go`
- **Extension:** `.go`
- **Size:** 29858 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `accRangeTest`
- `stRangesTest`
- `byteCodesTest`
- `trieNodesTest`
- `snapRequest`
- `TestSnapStatus`
- `TestSnapGetAccountRange`
- `hashAdd`
- `findNonEmptyStorageRoot`
- `TestSnapGetStorageRanges`
- `TestSnapGetByteCodes`
- `decodeNibbles`
- `hasTerm`
- `keybytesToHex`
- `hexToCompact`
- `TestSnapTrieNodes`
- `makeSnapPath`
- `snapGetAccountRange`
- `snapGetStorageRanges`
- `snapGetByteCodes`
- `snapGetTrieNodes`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[internal/utesting/utesting.go.md|internal/utesting/utesting.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package ethtest

import (
	"bytes"
...
```