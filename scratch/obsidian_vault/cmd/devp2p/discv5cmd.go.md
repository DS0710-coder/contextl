# discv5cmd.go

## Architecture Metrics
- **Path:** `cmd/devp2p/discv5cmd.go`
- **Extension:** `.go`
- **Size:** 3733 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `discv5Ping`
- `discv5Resolve`
- `discv5Crawl`
- `discv5Test`
- `discv5Listen`
- `startV5`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/devp2p/internal/v5test/discv5tests.go.md|cmd/devp2p/internal/v5test/discv5tests.go]]
- [[common/big.go.md|common/big.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package main

import (
	"errors"
...
```