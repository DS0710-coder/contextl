# server_test.go

## Architecture Metrics
- **Path:** `p2p/server_test.go`
- **Extension:** `.go`
- **Size:** 18215 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testTransport`
- `setupTransport`
- `fakeAddrListener`
- `fakeAddrConn`
- `newTestTransport`
- `doEncHandshake`
- `doProtoHandshake`
- `close`
- `startTestServer`
- `TestServerListen`
- `TestServerDial`
- `TestServerRemovePeerDisconnect`
- `TestServerAtCap`
- `TestServerPeerLimits`
- `TestServerSetupConn`
- `doEncHandshake`
- `doProtoHandshake`
- `close`
- `WriteMsg`
- `ReadMsg`
- `newkey`
- `randomID`
- `TestServerInboundThrottle`
- `TestServerDiscoveryV5FailureRollsBackV4`
- `listenFakeAddr`
- `Accept`
- `RemoteAddr`
- `syncAddPeer`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[internal/testlog/testlog.go.md|internal/testlog/testlog.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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
	"crypto/ecdsa"
...
```