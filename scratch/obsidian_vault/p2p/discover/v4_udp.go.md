# v4_udp.go

## Architecture Metrics
- **Path:** `p2p/discover/v4_udp.go`
- **Extension:** `.go`
- **Size:** 25217 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UDPv4`
- `replyMatcher`
- `reply`
- `packetHandlerV4`
- `ListenV4`
- `Self`
- `Close`
- `Resolve`
- `ourEndpoint`
- `ping`
- `Ping`
- `sendPing`
- `makePing`
- `LookupPubkey`
- `RandomNodes`
- `lookupRandom`
- `lookupSelf`
- `newRandomLookup`
- `newLookup`
- `findnode`
- `RequestENR`
- `TableBuckets`
- `pending`
- `handleReply`
- `loop`
- `send`
- `write`
- `readLoop`
- `handlePacket`
- `checkBond`
- `ensureBond`
- `nodeFromRPC`
- `nodeToRPC`
- `wrapPacket`
- `verifyPing`
- `handlePing`
- `verifyPong`
- `verifyFindnode`
- `handleFindnode`
- `verifyNeighbors`
- `verifyENRRequest`
- `handleENRRequest`
- `verifyENRResponse`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]

## Imported By (Dependents)
*Not imported by any file*

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
	"bytes"
...
```