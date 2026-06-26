# call_flat.go

## Architecture Metrics
- **Path:** `eth/tracers/native/call_flat.go`
- **Extension:** `.go`
- **Size:** 12152 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `flatCallFrame`
- `flatCallAction`
- `flatCallActionMarshaling`
- `flatCallResult`
- `flatCallResultMarshaling`
- `flatCallTracer`
- `flatCallTracerConfig`
- `init`
- `newFlatCallTracer`
- `OnEnter`
- `OnExit`
- `OnTxStart`
- `OnTxEnd`
- `GetResult`
- `Stop`
- `isPrecompiled`
- `flatFromNested`
- `newFlatCreate`
- `newFlatCall`
- `newFlatSelfdestruct`
- `fillCallFrameFromContext`
- `convertErrorToParity`
- `childTraceAddress`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package native

import (
	"encoding/json"
...
```