# era.go

## Architecture Metrics
- **Path:** `internal/era/era.go`
- **Extension:** `.go`
- **Size:** 5170 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 13
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadAtSeekCloser`
- `Iterator`
- `Builder`
- `Era`
- `ReadDir`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

## Imported By (Dependents)
- [[cmd/era/main.go.md|cmd/era/main.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[core/rawdb/eradb/eradb.go.md|core/rawdb/eradb/eradb.go]]
- [[internal/era/eradl/eradl.go.md|internal/era/eradl/eradl.go]]
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/execdb/era_test.go.md|internal/era/execdb/era_test.go]]
- [[internal/era/execdb/iterator.go.md|internal/era/execdb/iterator.go]]
- [[internal/era/execdb/reader.go.md|internal/era/execdb/reader.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[internal/era/onedb/iterator.go.md|internal/era/onedb/iterator.go]]
- [[internal/era/onedb/reader.go.md|internal/era/onedb/reader.go]]

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

package era

import (
	"fmt"
...
```