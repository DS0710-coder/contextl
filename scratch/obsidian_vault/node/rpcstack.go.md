# rpcstack.go

## Architecture Metrics
- **Path:** `node/rpcstack.go`
- **Extension:** `.go`
- **Size:** 18420 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `httpConfig`
- `wsConfig`
- `rpcEndpointConfig`
- `rpcHandler`
- `httpServer`
- `virtualHostHandler`
- `gzipResponseWriter`
- `ipcServer`
- `newHTTPServer`
- `setListenAddr`
- `listenAddr`
- `start`
- `ServeHTTP`
- `checkPath`
- `validatePrefix`
- `stop`
- `doStop`
- `enableRPC`
- `disableRPC`
- `enableWS`
- `stopWS`
- `disableWS`
- `rpcAllowed`
- `wsAllowed`
- `isWebsocket`
- `NewHTTPHandlerStack`
- `NewWSHandlerStack`
- `newCorsHandler`
- `newVHostHandler`
- `ServeHTTP`
- `init`
- `Header`
- `WriteHeader`
- `Write`
- `Flush`
- `close`
- `newGzipHandler`
- `newIPCServer`
- `start`
- `stop`
- `RegisterApis`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
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
	"compress/gzip"
...
```