# errors.go

## Architecture Metrics
- **Path:** `core/txpool/locals/errors.go`
- **Extension:** `.go`
- **Size:** 1640 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `IsTemporaryReject`

## Imports (Dependencies)
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]

## Imported By (Dependents)
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/backend.go.md|eth/backend.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

package locals

import (
	"errors"
...
```