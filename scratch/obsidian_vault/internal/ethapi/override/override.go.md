# override.go

## Architecture Metrics
- **Path:** `internal/ethapi/override/override.go`
- **Extension:** `.go`
- **Size:** 7062 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `OverrideAccount`
- `BlockOverrides`
- `has`
- `Apply`
- `Apply`
- `MakeHeader`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]

## Imported By (Dependents)
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/simulate_test.go.md|internal/ethapi/simulate_test.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package override

import (
	"errors"
...
```