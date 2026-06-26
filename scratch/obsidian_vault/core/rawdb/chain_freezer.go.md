# chain_freezer.go

## Architecture Metrics
- **Path:** `core/rawdb/chain_freezer.go`
- **Extension:** `.go`
- **Size:** 14852 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `chainFreezer`
- `newChainFreezer`
- `Close`
- `readHeadNumber`
- `readFinalizedNumber`
- `freezeThreshold`
- `freeze`
- `freezeRange`
- `Ancient`
- `tableTailGroup`
- `ReadAncients`
- `Ancients`
- `Tail`
- `AncientSize`
- `AncientRange`
- `AncientBytes`
- `ModifyAncients`
- `TruncateHead`
- `TruncateTail`
- `SyncAncient`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/eradb/eradb.go.md|core/rawdb/eradb/eradb.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package rawdb

import (
	"errors"
...
```