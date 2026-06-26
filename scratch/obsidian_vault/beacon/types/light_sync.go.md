# light_sync.go

## Architecture Metrics
- **Path:** `beacon/types/light_sync.go`
- **Extension:** `.go`
- **Size:** 10295 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `HeadInfo`
- `BootstrapData`
- `LightClientUpdate`
- `UpdateScore`
- `HeaderWithExecProof`
- `OptimisticUpdate`
- `FinalityUpdate`
- `ChainHeadEvent`
- `Validate`
- `Validate`
- `Score`
- `finalized`
- `BetterThan`
- `Validate`
- `SignedHeader`
- `Validate`
- `SignedHeader`
- `Validate`

## Imports (Dependencies)
- [[beacon/merkle/merkle.go.md|beacon/merkle/merkle.go]]
- [[beacon/params/params.go.md|beacon/params/params.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

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

package types

import (
	"errors"
...
```