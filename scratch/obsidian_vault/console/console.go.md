# console.go

## Architecture Metrics
- **Path:** `console/console.go`
- **Extension:** `.go`
- **Size:** 16741 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `Console`
- `New`
- `init`
- `initConsoleObject`
- `initWeb3`
- `initExtensions`
- `initAdmin`
- `clearHistory`
- `consoleOutput`
- `AutoCompleteInput`
- `Welcome`
- `Evaluate`
- `interruptHandler`
- `setSignalReceived`
- `clearSignalReceived`
- `StopInteractive`
- `Interactive`
- `readLines`
- `countIndents`
- `Stop`
- `writeHistory`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[console/prompt/prompter.go.md|console/prompt/prompter.go]]
- [[internal/jsre/deps/deps.go.md|internal/jsre/deps/deps.go]]
- [[internal/jsre/jsre.go.md|internal/jsre/jsre.go]]
- [[internal/web3ext/web3ext.go.md|internal/web3ext/web3ext.go]]
- [[log/format.go.md|log/format.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/geth/consolecmd.go.md|cmd/geth/consolecmd.go]]

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package console

import (
	"errors"
...
```