# dial.go

## Architecture Metrics
- **Path:** `p2p/dial.go`
- **Extension:** `.go`
- **Size:** 19611 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeDialer`
- `nodeResolver`
- `tcpDialer`
- `dialScheduler`
- `dialConfig`
- `dialTask`
- `dialError`
- `Dial`
- `withDefaults`
- `newDialScheduler`
- `stop`
- `addStatic`
- `removeStatic`
- `peerAdded`
- `peerRemoved`
- `inboundPending`
- `inboundCompleted`
- `loop`
- `readNodes`
- `logStats`
- `rearmHistoryTimer`
- `expireHistory`
- `freeDialSlots`
- `checkDial`
- `startStaticDials`
- `updateStaticPool`
- `addToStaticPool`
- `removeFromStaticPool`
- `dnsResolveHostname`
- `startDial`
- `newDialTask`
- `dest`
- `run`
- `isStatic`
- `resolve`
- `dial`
- `String`
- `cleanupDialErr`
- `nodeEndpointForLog`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]

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

package p2p

import (
	"context"
...
```