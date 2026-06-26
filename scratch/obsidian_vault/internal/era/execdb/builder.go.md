# builder.go

## Architecture Metrics
- **Path:** `internal/era/execdb/builder.go`
- **Extension:** `.go`
- **Size:** 11204 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Builder`
- `offsets`
- `NewBuilder`
- `Add`
- `AddRLP`
- `Accumulator`
- `Finalize`
- `uint256LE`
- `snappyWrite`
- `writeIndex`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[internal/era/e2store/e2store.go.md|internal/era/e2store/e2store.go]]
- [[internal/era/era.go.md|internal/era/era.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/era/main.go.md|cmd/era/main.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[core/rawdb/eradb/eradb.go.md|core/rawdb/eradb/eradb.go]]
- [[core/rawdb/eradb/eradb_test.go.md|core/rawdb/eradb/eradb_test.go]]

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

package execdb

// Ere file format specification.
//
...
```