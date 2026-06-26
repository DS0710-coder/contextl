# secure_trie.go

## Architecture Metrics
- **Path:** `trie/secure_trie.go`
- **Extension:** `.go`
- **Size:** 11413 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `preimageStore`
- `StateTrie`
- `NewSecure`
- `NewStateTrie`
- `MustGet`
- `GetAccount`
- `GetAccountByHash`
- `PrefetchAccount`
- `GetStorage`
- `PrefetchStorage`
- `GetNode`
- `MustUpdate`
- `UpdateStorage`
- `UpdateAccount`
- `UpdateContractCode`
- `MustDelete`
- `DeleteStorage`
- `DeleteAccount`
- `GetKey`
- `Witness`
- `Commit`
- `Hash`
- `Copy`
- `NodeIterator`
- `MustNodeIterator`
- `IsUBT`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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
	"github.com/ethereum/go-ethereum/common"
...
```