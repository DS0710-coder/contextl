# rpcstack_test.go

## Architecture Metrics
- **Path:** `node/rpcstack_test.go`
- **Extension:** `.go`
- **Size:** 19493 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `originTest`
- `gzipTest`
- `testService`
- `TestCorsHandler`
- `TestVhosts`
- `splitAndTrim`
- `TestWebsocketOrigins`
- `TestIsWebsocket`
- `Test_checkPath`
- `createAndStartServer`
- `wsRequest`
- `rpcRequest`
- `batchRpcRequest`
- `baseRpcRequest`
- `Valid`
- `TestJWT`
- `TestGzipHandler`
- `TestHTTPWriteTimeout`
- `TestHTTP2H2C`
- `apis`
- `Greet`
- `Sleep`

## Imports (Dependencies)
- [[internal/testlog/testlog.go.md|internal/testlog/testlog.go]]
- [[log/format.go.md|log/format.go]]
- [[rpc/client.go.md|rpc/client.go]]

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

package node

import (
	"bytes"
...
```