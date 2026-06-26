# scheduler.go

## Architecture Metrics
- **Path:** `beacon/light/request/scheduler.go`
- **Extension:** `.go`
- **Size:** 13511 bytes
- **Centrality Score:** 0.0092
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Module`
- `Requester`
- `Scheduler`
- `Server`
- `ServerAndID`
- `targetData`
- `pendingRequest`
- `requester`
- `NewScheduler`
- `RegisterTarget`
- `RegisterModule`
- `RegisterServer`
- `UnregisterServer`
- `Start`
- `Stop`
- `syncLoop`
- `targetChanged`
- `processRound`
- `Trigger`
- `addEvent`
- `filterEvents`
- `closePending`
- `CanSendTo`
- `Send`
- `Fail`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[beacon/blsync/block_sync_test.go.md|beacon/blsync/block_sync_test.go]]
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/light/api/api_server.go.md|beacon/light/api/api_server.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/light/sync/head_sync_test.go.md|beacon/light/sync/head_sync_test.go]]
- [[beacon/light/sync/test_helpers.go.md|beacon/light/sync/test_helpers.go]]
- [[beacon/light/sync/types.go.md|beacon/light/sync/types.go]]
- [[beacon/light/sync/update_sync.go.md|beacon/light/sync/update_sync.go]]
- [[beacon/light/sync/update_sync_test.go.md|beacon/light/sync/update_sync_test.go]]

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package request

import (
	"sync"
...
```