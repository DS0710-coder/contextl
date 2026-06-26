# pebble.go

## Architecture Metrics
- **Path:** `ethdb/pebble/pebble.go`
- **Extension:** `.go`
- **Size:** 31011 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 12
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Database`
- `panicLogger`
- `batch`
- `pebbleIterator`
- `onCompactionBegin`
- `onCompactionEnd`
- `onWriteStallBegin`
- `onWriteStallEnd`
- `Infof`
- `Errorf`
- `Fatalf`
- `New`
- `Close`
- `Has`
- `Get`
- `Put`
- `Delete`
- `DeleteRange`
- `NewBatch`
- `NewBatchWithSize`
- `upperBound`
- `Stat`
- `Compact`
- `Path`
- `SyncKeyValue`
- `meter`
- `Put`
- `Delete`
- `DeleteRange`
- `ValueSize`
- `Write`
- `Reset`
- `Replay`
- `Close`
- `NewIterator`
- `Next`
- `Error`
- `Key`
- `Value`
- `Release`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/blockchain_repair_test.go.md|core/blockchain_repair_test.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/blockchain_snapshot_test.go.md|core/blockchain_snapshot_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[ethdb/pebble/pebble_test.go.md|ethdb/pebble/pebble_test.go]]
- [[ethdb/pebble/pebble_v1.go.md|ethdb/pebble/pebble_v1.go]]
- [[ethdb/pebble/version.go.md|ethdb/pebble/version.go]]
- [[ethdb/pebble/version_test.go.md|ethdb/pebble/version_test.go]]
- [[node/database.go.md|node/database.go]]

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

// Package pebble implements the key-value database layer based on pebble.
package pebble

import (
...
```