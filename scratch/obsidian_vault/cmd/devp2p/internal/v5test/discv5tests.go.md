# discv5tests.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/v5test/discv5tests.go`
- **Extension:** `.go`
- **Size:** 13272 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Suite`
- `bystander`
- `listen1`
- `listen2`
- `AllTests`
- `TestPing`
- `checkPong`
- `TestPingLargeRequestID`
- `TestPingMultiIP`
- `TestHandshakeResend`
- `TestTalkRequest`
- `TestFindnodeZeroDistance`
- `TestFindnodeResults`
- `newBystander`
- `id`
- `close`
- `loop`
- `notifyLive`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[internal/utesting/utesting.go.md|internal/utesting/utesting.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]

## Imported By (Dependents)
- [[cmd/devp2p/discv5cmd.go.md|cmd/devp2p/discv5cmd.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package v5test

import (
	"bytes"
...
```