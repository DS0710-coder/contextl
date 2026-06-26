# suite.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/ethtest/suite.go`
- **Extension:** `.go`
- **Size:** 39860 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Suite`
- `NewSuite`
- `EthTests`
- `SnapTests`
- `Snap2Tests`
- `TestStatus`
- `headersMatch`
- `TestGetBlockHeaders`
- `TestGetNonexistentBlockHeaders`
- `TestSimultaneousRequests`
- `TestSameRequestID`
- `checkHeadersAgainstChain`
- `collectHeaderResponses`
- `TestZeroRequestID`
- `TestGetBlockBodies`
- `TestGetReceipts`
- `TestGetLargeReceipts`
- `randBuf`
- `TestMaliciousHandshake`
- `TestBlockRangeUpdateInvalid`
- `TestBlockRangeUpdateFuture`
- `TestBlockRangeUpdateHistoryExp`
- `TestTransaction`
- `TestInvalidTxs`
- `TestLargeTxRequest`
- `TestNewPooledTxs`
- `makeSidecar`
- `makeBlobTxs`
- `TestBlobViolations`
- `mangleSidecar`
- `TestBlobTxWithoutSidecar`
- `TestBlobTxWithMismatchedSidecar`
- `readUntil`
- `readUntilDisconnect`
- `testBadBlobTx`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[internal/utesting/utesting.go.md|internal/utesting/utesting.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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
	"context"
...
```