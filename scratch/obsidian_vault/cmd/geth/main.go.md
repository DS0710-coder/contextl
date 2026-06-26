# main.go

## Architecture Metrics
- **Path:** `cmd/geth/main.go`
- **Extension:** `.go`
- **Size:** 10375 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `init`
- `main`
- `prepare`
- `geth`
- `startNode`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[console/prompt/prompter.go.md|console/prompt/prompter.go]]
- [[eth/tracers/js/bigint.go.md|eth/tracers/js/bigint.go]]
- [[eth/tracers/live.go.md|eth/tracers/live.go]]
- [[eth/tracers/native/4byte.go.md|eth/tracers/native/4byte.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

// geth is a command-line client for Ethereum.
package main

import (
...
```