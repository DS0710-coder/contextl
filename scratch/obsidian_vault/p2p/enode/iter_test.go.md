# iter_test.go

## Architecture Metrics
- **Path:** `p2p/enode/iter_test.go`
- **Extension:** `.go`
- **Size:** 7935 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `genIter`
- `callCountIter`
- `TestReadNodes`
- `TestReadNodesCycle`
- `TestFilterNodes`
- `checkNodes`
- `TestFairMix`
- `testMixerFairness`
- `TestFairMixNextFromAll`
- `TestFairMixEmpty`
- `TestFairMixRemoveSource`
- `TestFairMixSourceName`
- `TestFairMixNestedSourceName`
- `Next`
- `Node`
- `Close`
- `TestFairMixClose`
- `testMixerClose`
- `idPrefixDistribution`
- `approxEqual`
- `Next`
- `Node`
- `Close`
- `testNode`
- `Next`

## Imports (Dependencies)
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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
	"encoding/binary"
...
```