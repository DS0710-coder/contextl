# eradb_test.go

## Architecture Metrics
- **Path:** `core/rawdb/eradb/eradb_test.go`
- **Extension:** `.go`
- **Size:** 5724 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestEraDatabase`
- `TestEreDatabase`
- `TestEreDatabaseNoReceipts`
- `convertEra1ToEre`
- `TestEraDatabaseConcurrentOpen`
- `TestEraDatabaseConcurrentOpenClose`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[core/types.go.md|core/types.go]]
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

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
// along with the go-ethereum library. If not, see <http://www.gnu.org/licenses/>.

package eradb

import (
	"math/big"
...
```