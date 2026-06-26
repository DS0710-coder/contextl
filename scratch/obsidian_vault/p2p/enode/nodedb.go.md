# nodedb.go

## Architecture Metrics
- **Path:** `p2p/enode/nodedb.go`
- **Extension:** `.go`
- **Size:** 14674 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DB`
- `OpenDB`
- `newMemoryDB`
- `newPersistentDB`
- `nodeKey`
- `splitNodeKey`
- `nodeItemKey`
- `splitNodeItemKey`
- `v5Key`
- `localItemKey`
- `fetchInt64`
- `storeInt64`
- `fetchUint64`
- `storeUint64`
- `Node`
- `mustDecodeNode`
- `UpdateNode`
- `NodeSeq`
- `Resolve`
- `DeleteNode`
- `deleteRange`
- `ensureExpirer`
- `expirer`
- `expireNodes`
- `LastPingReceived`
- `UpdateLastPingReceived`
- `LastPongReceived`
- `UpdateLastPongReceived`
- `FindFails`
- `UpdateFindFails`
- `FindFailsV5`
- `UpdateFindFailsV5`
- `localSeq`
- `storeLocalSeq`
- `QuerySeeds`
- `nextNode`
- `Close`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[ethdb/leveldb/leveldb.go.md|ethdb/leveldb/leveldb.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[signer/storage/storage.go.md|signer/storage/storage.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package enode

import (
	"bytes"
...
```