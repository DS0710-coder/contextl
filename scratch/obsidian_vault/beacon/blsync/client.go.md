# client.go

## Architecture Metrics
- **Path:** `beacon/blsync/client.go`
- **Extension:** `.go`
- **Size:** 3735 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Client`
- `NewClient`
- `SetEngineRPC`
- `Start`
- `Stop`

## Imports (Dependencies)
- [[beacon/light/api/api_server.go.md|beacon/light/api/api_server.go]]
- [[beacon/light/canonical.go.md|beacon/light/canonical.go]]
- [[beacon/light/request/scheduler.go.md|beacon/light/request/scheduler.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/params/params.go.md|beacon/params/params.go]]
- [[beacon/types/beacon_block.go.md|beacon/types/beacon_block.go]]
- [[common/big.go.md|common/big.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[ethdb/memorydb/memorydb.go.md|ethdb/memorydb/memorydb.go]]
- [[event/event.go.md|event/event.go]]
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
	"github.com/ethereum/go-ethereum/beacon/light"
...
```