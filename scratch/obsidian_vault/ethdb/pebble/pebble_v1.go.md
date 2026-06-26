# pebble_v1.go

## Architecture Metrics
- **Path:** `ethdb/pebble/pebble_v1.go`
- **Extension:** `.go`
- **Size:** 29295 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `V1Database`
- `v1batch`
- `v1pebbleIterator`
- `onCompactionBegin`
- `onCompactionEnd`
- `onWriteStallBegin`
- `onWriteStallEnd`
- `NewV1`
- `Close`
- `Has`
- `Get`
- `Put`
- `Delete`
- `DeleteRange`
- `NewBatch`
- `NewBatchWithSize`
- `Stat`
- `Compact`
- `Path`
- `SyncKeyValue`
- `NewIterator`
- `meter`
- `Put`
- `Delete`
- `DeleteRange`
- `ValueSize`
- `Write`
- `Reset`
- `Replay`
- `Close`
- `Next`
- `Error`
- `Key`
- `Value`
- `Release`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

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

// Legacy pebble v1 wrapper. This file mirrors pebble.go but with V1-prefixed
// types so that it can coexist alongside a future v2 variant in the same package.

package pebble
...
```