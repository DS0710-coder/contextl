# common.go

## Architecture Metrics
- **Path:** `p2p/discover/common.go`
- **Extension:** `.go`
- **Size:** 4452 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UDPConn`
- `Config`
- `ReadPacket`
- `randomSource`
- `reseedingRandom`
- `withDefaults`
- `ListenUDP`
- `seed`
- `Intn`
- `Int63n`
- `Shuffle`
- `iterList`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]

## Imported By (Dependents)
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/devp2p/discv5cmd.go.md|cmd/devp2p/discv5cmd.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/server.go.md|p2p/server.go]]

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

package discover

import (
	"container/list"
...
```