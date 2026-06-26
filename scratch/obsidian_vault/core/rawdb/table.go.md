# table.go

## Architecture Metrics
- **Path:** `core/rawdb/table.go`
- **Extension:** `.go`
- **Size:** 10661 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `table`
- `tableBatch`
- `tableReplayer`
- `tableIterator`
- `NewTable`
- `Close`
- `Has`
- `Get`
- `Ancient`
- `AncientRange`
- `AncientBytes`
- `Ancients`
- `Tail`
- `AncientSize`
- `ModifyAncients`
- `ReadAncients`
- `TruncateHead`
- `TruncateTail`
- `SyncAncient`
- `AncientDatadir`
- `Put`
- `Delete`
- `DeleteRange`
- `NewIterator`
- `Stat`
- `Compact`
- `SyncKeyValue`
- `NewBatch`
- `NewBatchWithSize`
- `Put`
- `Delete`
- `DeleteRange`
- `ValueSize`
- `Write`
- `Reset`
- `Close`
- `Put`
- `Delete`
- `Replay`
- `Next`
- `Error`
- `Key`
- `Value`
- `Release`

## Imports (Dependencies)
- [[ethdb/batch.go.md|ethdb/batch.go]]

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

package rawdb

import (
	"github.com/ethereum/go-ethereum/ethdb"
...
```