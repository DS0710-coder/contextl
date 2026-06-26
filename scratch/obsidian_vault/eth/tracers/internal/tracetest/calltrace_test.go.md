# calltrace_test.go

## Architecture Metrics
- **Path:** `eth/tracers/internal/tracetest/calltrace_test.go`
- **Extension:** `.go`
- **Size:** 14992 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `callLog`
- `callTrace`
- `callTracerTest`
- `simpleResult`
- `TestCallTracerLegacy`
- `TestCallTracerNative`
- `TestCallTracerNativeWithLog`
- `testCallTracer`
- `BenchmarkTracers`
- `benchTracer`
- `TestInternals`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[tests/block_test.go.md|tests/block_test.go]]

## Imported By (Dependents)
- [[internal/telemetry/telemetry_test.go.md|internal/telemetry/telemetry_test.go]]
- [[rpc/tracing_test.go.md|rpc/tracing_test.go]]

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

package tracetest

import (
	"encoding/json"
...
```