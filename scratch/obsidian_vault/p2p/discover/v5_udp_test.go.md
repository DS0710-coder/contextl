# v5_udp_test.go

## Architecture Metrics
- **Path:** `p2p/discover/v5_udp_test.go`
- **Extension:** `.go`
- **Size:** 30743 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BadIdentityScheme`
- `udpV5Test`
- `testCodec`
- `testCodecFrame`
- `TestUDPv5_lookupE2E`
- `startLocalhostV5`
- `TestUDPv5_pingHandling`
- `TestUDPv5_unknownPacket`
- `TestUDPv5_unknownPacketKnownNode`
- `TestUDPv5_handshakeRepeatChallenge`
- `TestUDPv5_findnodeHandling`
- `expectNodes`
- `TestUDPv5_pingCall`
- `TestUDPv5_findnodeCall`
- `Verify`
- `NodeAddr`
- `TestUDPv5_findnodeCall_InvalidNodes`
- `TestUDPv5_callResend`
- `TestUDPv5_multipleHandshakeRounds`
- `TestUDPv5_callTimeoutReset`
- `TestUDPv5_talkHandling`
- `TestUDPv5_talkRequest`
- `TestUDPv5_lookupDistances`
- `TestUDPv5_lookup`
- `TestUDPv5_LocalNode`
- `TestUDPv5_PingWithIPV4MappedAddress`
- `Encode`
- `CurrentChallenge`
- `Decode`
- `SessionNode`
- `decodeFrame`
- `newUDPV5Test`
- `packetIn`
- `packetInFrom`
- `getNode`
- `waitPacketOut`
- `close`

## Imports (Dependencies)
- [[internal/testlog/testlog.go.md|internal/testlog/testlog.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

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