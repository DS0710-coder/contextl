# api.go

## Architecture Metrics
- **Path:** `internal/debug/api.go`
- **Extension:** `.go`
- **Size:** 8957 bytes
- **Centrality Score:** 0.0026
- **In-Degree (Imported By):** 19
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `HandlerT`
- `Verbosity`
- `Vmodule`
- `MemStats`
- `GcStats`
- `CpuProfile`
- `StartCPUProfile`
- `StopCPUProfile`
- `GoTrace`
- `BlockProfile`
- `SetBlockProfileRate`
- `WriteBlockProfile`
- `MutexProfile`
- `SetMutexProfileFraction`
- `WriteMutexProfile`
- `WriteMemProfile`
- `Stacks`
- `FreeOSMemory`
- `SetGCPercent`
- `SetMemoryLimit`
- `writeProfile`
- `expandHome`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[cmd/blsync/main.go.md|cmd/blsync/main.go]]
- [[cmd/devp2p/main.go.md|cmd/devp2p/main.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/keeper/main.go.md|cmd/keeper/main.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/workload/main.go.md|cmd/workload/main.go]]
- [[common/debug.go.md|common/debug.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/debug/loudpanic.go.md|internal/debug/loudpanic.go]]
- [[internal/version/vcs.go.md|internal/version/vcs.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[metrics/debug.go.md|metrics/debug.go]]
- [[metrics/debug_test.go.md|metrics/debug_test.go]]
- [[node/api.go.md|node/api.go]]

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

// Package debug interfaces Go runtime debugging facilities.
// This package is mostly glue code making these facilities available
// through the CLI and RPC subsystem. If you want to use them from Go code,
// use package runtime instead.
...
```