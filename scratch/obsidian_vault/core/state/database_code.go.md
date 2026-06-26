# database_code.go

## Architecture Metrics
- **Path:** `core/state/database_code.go`
- **Extension:** `.go`
- **Size:** 7198 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `codeCache`
- `CodeReader`
- `CodeBatch`
- `CodeDB`
- `newCodeCache`
- `Get`
- `GetSize`
- `Put`
- `newCodeReader`
- `Has`
- `Code`
- `CodeSize`
- `CodeWithPrefix`
- `GetCodeStats`
- `newCodeBatch`
- `newCodeBatchWithSize`
- `Put`
- `Commit`
- `NewCodeDB`
- `Reader`
- `NewBatch`
- `NewBatchWithSize`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package state

import (
	"sync/atomic"
...
```