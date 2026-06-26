# nodesetcmd.go

## Architecture Metrics
- **Path:** `cmd/devp2p/nodesetcmd.go`
- **Extension:** `.go`
- **Size:** 6849 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `nodeFilterC`
- `nodesetInfo`
- `showAttributeCounts`
- `nodesetFilter`
- `parseFilters`
- `parseFilterLimit`
- `andFilter`
- `trueFilter`
- `ipFilter`
- `minAgeFilter`
- `ethFilter`
- `lesFilter`
- `snapFilter`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/forkid/forkid.go.md|core/forkid/forkid.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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