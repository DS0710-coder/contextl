# e2store.go

## Architecture Metrics
- **Path:** `internal/era/e2store/e2store.go`
- **Extension:** `.go`
- **Size:** 6255 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Entry`
- `Writer`
- `Reader`
- `NewWriter`
- `Write`
- `NewReader`
- `Read`
- `ReadAt`
- `ReaderAt`
- `LengthAt`
- `ReadMetadataAt`
- `Find`
- `FindAll`
- `SkipN`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/execdb/era_test.go.md|internal/era/execdb/era_test.go]]
- [[internal/era/execdb/iterator.go.md|internal/era/execdb/iterator.go]]
- [[internal/era/execdb/reader.go.md|internal/era/execdb/reader.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[internal/era/onedb/reader.go.md|internal/era/onedb/reader.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package e2store

import (
	"encoding/binary"
...
```