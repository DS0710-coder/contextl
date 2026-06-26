# hooks.go

## Architecture Metrics
- **Path:** `core/tracing/hooks.go`
- **Extension:** `.go`
- **Size:** 24826 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `OpContext`
- `StateDB`
- `VMContext`
- `BlockEvent`
- `StateUpdate`
- `AccountChange`
- `StorageChange`
- `ContractCode`
- `CodeChange`
- `TrieNodeChange`
- `Hooks`
- `Gas`
- `HasGasHook`
- `EmitGasChange`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[node/api.go.md|node/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

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

// Package tracing defines hooks for 'live tracing' of block processing and transaction
// execution. Here we define the low-level [Hooks] object that carries hooks which are
// invoked by the go-ethereum core at various points in the state transition.
//
...
```