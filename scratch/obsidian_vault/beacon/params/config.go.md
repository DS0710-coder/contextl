# config.go

## Architecture Metrics
- **Path:** `beacon/params/config.go`
- **Extension:** `.go`
- **Size:** 8364 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ClientConfig`
- `ChainConfig`
- `Fork`
- `ForkAtEpoch`
- `AddFork`
- `LoadForks`
- `computeDomain`
- `domain`
- `SigningRoot`
- `Len`
- `Swap`
- `Less`
- `SetCheckpointFile`
- `SaveCheckpointToFile`

## Imports (Dependencies)
- [[beacon/merkle/merkle.go.md|beacon/merkle/merkle.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package params

import (
	"crypto/sha256"
...
```