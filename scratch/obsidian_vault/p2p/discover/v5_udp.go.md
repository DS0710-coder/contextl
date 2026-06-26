# v5_udp.go

## Architecture Metrics
- **Path:** `p2p/discover/v5_udp.go`
- **Extension:** `.go`
- **Size:** 29818 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `codecV5`
- `UDPv5`
- `sendRequest`
- `callV5`
- `callTimeout`
- `ListenV5`
- `newUDPv5`
- `Self`
- `Close`
- `Resolve`
- `ResolveNodeId`
- `AllNodes`
- `AddKnownNode`
- `DeleteNode`
- `LocalNode`
- `RegisterTalkHandler`
- `TalkRequest`
- `TalkRequestToID`
- `RandomNodes`
- `Lookup`
- `lookupRandom`
- `lookupSelf`
- `newRandomLookup`
- `newLookup`
- `lookupWorker`
- `lookupDistances`
- `ping`
- `Ping`
- `RequestENR`
- `Findnode`
- `waitForNodes`
- `verifyResponseNode`
- `callToNode`
- `callToID`
- `initCall`
- `callDone`
- `dispatch`
- `startResponseTimeout`
- `sendNextCall`
- `sendCall`
- `sendResponse`
- `sendFromAnotherThread`
- `send`
- `readLoop`
- `dispatchReadPacket`
- `handlePacket`
- `handleCallResponse`
- `GetNode`
- `Nodes`
- `handle`
- `handleUnknown`
- `handleWhoareyou`
- `matchWithCall`
- `handlePing`
- `handleFindnode`
- `collectTableNodes`
- `packNodes`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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
	"bytes"
...
```