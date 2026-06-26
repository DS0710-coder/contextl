# test_hash.go

## Architecture Metrics
- **Path:** `internal/blocktest/test_hash.go`
- **Extension:** `.go`
- **Size:** 1952 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testHasher`
- `NewHasher`
- `Reset`
- `Update`
- `Hash`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]

## Imported By (Dependents)
- [[core/rawdb/accessors_indexes_test.go.md|core/rawdb/accessors_indexes_test.go]]
- [[core/types/block_test.go.md|core/types/block_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

// Package utesting provides a standalone replacement for package testing.
//
// This package exists because package testing cannot easily be embedded into a
// standalone go program. It provides an API that mirrors the standard library
...
```