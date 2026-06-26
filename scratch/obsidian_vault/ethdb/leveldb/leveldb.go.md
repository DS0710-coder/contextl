# leveldb.go

## Architecture Metrics
- **Path:** `ethdb/leveldb/leveldb.go`
- **Extension:** `.go`
- **Size:** 20940 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Database`
- `batch`
- `replayer`
- `New`
- `NewCustom`
- `configureOptions`
- `Close`
- `Has`
- `Get`
- `Put`
- `Delete`
- `DeleteRange`
- `NewBatch`
- `NewBatchWithSize`
- `NewIterator`
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
- `Put`
- `Delete`
- `DeleteRange`
- `bytesPrefixRange`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/leveldb/leveldb.go.md|ethdb/leveldb/leveldb.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
- [[ethdb/leveldb/leveldb.go.md|ethdb/leveldb/leveldb.go]]
- [[ethdb/leveldb/leveldb_test.go.md|ethdb/leveldb/leveldb_test.go]]
- [[node/database.go.md|node/database.go]]
- [[p2p/enode/nodedb.go.md|p2p/enode/nodedb.go]]

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

//go:build !js && !wasip1
// +build !js,!wasip1

// Package leveldb implements the key-value database layer based on LevelDB.
...
```