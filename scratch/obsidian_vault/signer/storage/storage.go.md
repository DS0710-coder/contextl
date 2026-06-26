# storage.go

## Architecture Metrics
- **Path:** `signer/storage/storage.go`
- **Extension:** `.go`
- **Size:** 2596 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Storage`
- `EphemeralStorage`
- `NoStorage`
- `Put`
- `Get`
- `Del`
- `NewEphemeralStorage`
- `Put`
- `Del`
- `Get`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[ethdb/leveldb/leveldb_test.go.md|ethdb/leveldb/leveldb_test.go]]
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

package storage

import "errors"

...
```