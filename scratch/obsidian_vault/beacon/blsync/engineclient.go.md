# engineclient.go

## Architecture Metrics
- **Path:** `beacon/blsync/engineclient.go`
- **Extension:** `.go`
- **Size:** 5453 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `engineClient`
- `startEngineClient`
- `stop`
- `updateLoop`
- `callNewPayload`
- `collectBlobHashes`
- `callForkchoiceUpdated`

## Imports (Dependencies)
- [[beacon/engine/bapl_encode.go.md|beacon/engine/bapl_encode.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/params/params.go.md|beacon/params/params.go]]
- [[beacon/types/beacon_block.go.md|beacon/types/beacon_block.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package blsync

import (
	"context"
...
```