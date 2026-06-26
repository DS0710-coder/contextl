# database.go

## Architecture Metrics
- **Path:** `core/rawdb/database.go`
- **Extension:** `.go`
- **Size:** 31339 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `freezerdb`
- `nofreezedb`
- `OpenOptions`
- `stat`
- `AncientDatadir`
- `Close`
- `Freeze`
- `Ancient`
- `AncientRange`
- `AncientBytes`
- `Ancients`
- `Tail`
- `AncientSize`
- `ModifyAncients`
- `TruncateHead`
- `TruncateTail`
- `SyncAncient`
- `ReadAncients`
- `AncientDatadir`
- `NewDatabase`
- `resolveChainFreezerDir`
- `resolveChainEraDir`
- `NewDatabaseWithFreezer`
- `Open`
- `NewMemoryDatabase`
- `PreexistingDatabase`
- `fileExists`
- `anyFileMatches`
- `String`
- `Percentage`
- `empty`
- `add`
- `sizeString`
- `countString`
- `InspectDatabase`
- `printChainMetadata`
- `ReadChainMetadata`
- `SafeDeleteRange`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/memorydb/memorydb.go.md|ethdb/memorydb/memorydb.go]]
- [[internal/tablewriter/database_tablewriter.go.md|internal/tablewriter/database_tablewriter.go]]
- [[log/format.go.md|log/format.go]]

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
	"bytes"
...
```