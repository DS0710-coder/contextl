# tracer_test.go

## Architecture Metrics
- **Path:** `eth/tracers/js/tracer_test.go`
- **Extension:** `.go`
- **Size:** 16928 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `dummyStatedb`
- `vmContext`
- `GetRefund`
- `GetBalance`
- `testCtx`
- `runTrace`
- `TestTracer`
- `TestHalt`
- `TestHaltBetweenSteps`
- `TestNoStepExec`
- `TestIsPrecompile`
- `TestEnterExit`
- `TestSetup`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package js

import (
	"encoding/json"
...
```