# node.go

## Architecture Metrics
- **Path:** `p2p/enode/node.go`
- **Extension:** `.go`
- **Size:** 9491 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Node`
- `New`
- `newNodeWithID`
- `validIP`
- `localityScore`
- `setIP4`
- `setIPv4Ports`
- `setIP6`
- `MustParse`
- `Parse`
- `ID`
- `Seq`
- `Load`
- `IP`
- `IPAddr`
- `UDP`
- `TCP`
- `WithHostname`
- `Hostname`
- `UDPEndpoint`
- `TCPEndpoint`
- `QUICEndpoint`
- `Pubkey`
- `Record`
- `ValidateComplete`
- `String`
- `MarshalText`
- `UnmarshalText`
- `Bytes`
- `String`
- `GoString`
- `TerminalString`
- `MarshalText`
- `UnmarshalText`
- `HexID`
- `ParseID`
- `DistCmp`
- `LogDist`

## Imports (Dependencies)
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

package enode

import (
	"crypto/ecdsa"
...
```