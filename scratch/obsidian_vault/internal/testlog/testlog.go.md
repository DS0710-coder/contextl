# testlog.go

## Architecture Metrics
- **Path:** `internal/testlog/testlog.go`
- **Extension:** `.go`
- **Size:** 5282 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 8
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `T`
- `logger`
- `bufHandler`
- `Handle`
- `Enabled`
- `WithAttrs`
- `WithGroup`
- `Logger`
- `Handler`
- `Write`
- `Enabled`
- `Trace`
- `Log`
- `Debug`
- `Info`
- `Warn`
- `Error`
- `Crit`
- `With`
- `New`
- `terminalFormat`
- `flush`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[node/rpcstack_test.go.md|node/rpcstack_test.go]]
- [[p2p/dial_test.go.md|p2p/dial_test.go]]
- [[p2p/discover/table_test.go.md|p2p/discover/table_test.go]]
- [[p2p/discover/v4_udp_test.go.md|p2p/discover/v4_udp_test.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/server_nat_test.go.md|p2p/server_nat_test.go]]
- [[p2p/server_test.go.md|p2p/server_test.go]]

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

// Package testlog provides a log handler for unit tests.
package testlog

import (
...
```