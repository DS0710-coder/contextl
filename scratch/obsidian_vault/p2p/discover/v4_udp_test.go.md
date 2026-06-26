# v4_udp_test.go

## Architecture Metrics
- **Path:** `p2p/discover/v4_udp_test.go`
- **Extension:** `.go`
- **Size:** 21283 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `udpTest`
- `dgramPipe`
- `dgram`
- `newUDPTest`
- `close`
- `packetIn`
- `packetInFrom`
- `waitPacketOut`
- `TestUDPv4_packetErrors`
- `TestUDPv4_pingTimeout`
- `TestUDPv4_RequestENRNoUDPEndpoint`
- `Kind`
- `Name`
- `TestUDPv4_responseTimeouts`
- `TestUDPv4_findnodeTimeout`
- `TestUDPv4_findnode`
- `TestUDPv4_findnodeMultiReply`
- `TestUDPv4_pingMatch`
- `TestUDPv4_pingMatchIP`
- `TestUDPv4_successfulPing`
- `TestUDPv4_EIP868`
- `TestUDPv4_smallNetConvergence`
- `startLocalhostV4`
- `newpipe`
- `WriteToUDPAddrPort`
- `ReadFromUDPAddrPort`
- `Close`
- `LocalAddr`
- `receive`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[internal/testlog/testlog.go.md|internal/testlog/testlog.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]

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

package discover

import (
	"bytes"
...
```