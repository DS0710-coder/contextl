# history_index_block.go

## Architecture Metrics
- **Path:** `triedb/pathdb/history_index_block.go`
- **Extension:** `.go`
- **Size:** 15713 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `indexBlockDesc`
- `blockReader`
- `blockWriter`
- `newIndexBlockDesc`
- `empty`
- `encode`
- `decode`
- `copy`
- `parseIndexBlock`
- `newBlockReader`
- `readGreaterThan`
- `newBlockWriter`
- `setBitmap`
- `append`
- `scanSection`
- `sectionLast`
- `sectionSearch`
- `rebuildBitmap`
- `pop`
- `empty`
- `estimateFull`
- `last`
- `finish`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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
// along with the go-ethereum library. If not, see <http://www.gnu.org/licenses/

package pathdb

import (
	"bytes"
...
```