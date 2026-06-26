# canonical.go

## Architecture Metrics
- **Path:** `beacon/light/canonical.go`
- **Extension:** `.go`
- **Size:** 4395 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `canonicalStore`
- `newCanonicalStore`
- `databaseKey`
- `add`
- `deleteFrom`
- `get`

## Imports (Dependencies)
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/light/sync/test_helpers.go.md|beacon/light/sync/test_helpers.go]]
- [[beacon/light/sync/update_sync.go.md|beacon/light/sync/update_sync.go]]

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

package light

import (
	"encoding/binary"
...
```