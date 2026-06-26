# handlers.go

## Architecture Metrics
- **Path:** `eth/protocols/eth/handlers.go`
- **Extension:** `.go`
- **Size:** 22831 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockBodyHashes`
- `derivableRawList`
- `handleGetBlockHeaders`
- `ServiceGetBlockHeadersQuery`
- `serviceNonContiguousBlockHeaderQuery`
- `serviceContiguousBlockHeaderQuery`
- `handleGetBlockBodies`
- `ServiceGetBlockBodiesQuery`
- `handleGetReceipts69`
- `handleGetReceipts70`
- `ServiceGetReceiptsQuery69`
- `serviceGetReceiptsQuery70`
- `handleBlockHeaders`
- `handleBlockBodies`
- `hashBodyParts`
- `newDerivableRawList`
- `Len`
- `EncodeIndex`
- `writeTxForHash`
- `handleReceipts69`
- `handleReceipts70`
- `dispatchReceipts`
- `handleNewPooledTransactionHashes`
- `handleGetPooledTransactions`
- `answerGetPooledTransactions`
- `handleTransactions`
- `handlePooledTransactions`
- `handleBlockRangeUpdate`
- `handleGetBlockAccessLists`
- `serviceGetBlockAccessListsQuery`
- `handleBlockAccessLists`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[p2p/tracker/tracker.go.md|p2p/tracker/tracker.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package eth

import (
	"bytes"
...
```