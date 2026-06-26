# bal_apply.go

## Architecture Metrics
- **Path:** `eth/protocols/snap/bal_apply.go`
- **Extension:** `.go`
- **Size:** 6692 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `verifyAccessList`
- `isFetched`
- `isStorageFetched`
- `applyAccessList`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/conn.go.md|cmd/devp2p/internal/ethtest/conn.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/snap2.go.md|cmd/devp2p/internal/ethtest/snap2.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_snap.go.md|eth/handler_snap.go]]
- [[eth/peer.go.md|eth/peer.go]]
- [[eth/peerset.go.md|eth/peerset.go]]
- [[eth/sync_test.go.md|eth/sync_test.go]]

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package snap

import (
	"bytes"
...
```