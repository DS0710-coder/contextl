# keccak256_preimage_test.go

## Architecture Metrics
- **Path:** `eth/tracers/native/keccak256_preimage_test.go`
- **Extension:** `.go`
- **Size:** 12649 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `mockOpContext`
- `MemoryData`
- `StackData`
- `Address`
- `Caller`
- `CallValue`
- `CallInput`
- `ContractCode`
- `TestKeccak256PreimageTracerCreation`
- `TestKeccak256PreimageTracerInitialResult`
- `TestKeccak256PreimageTracerSingleKeccak`
- `TestKeccak256PreimageTracerMultipleKeccak`
- `TestKeccak256PreimageTracerNonKeccakOpcodes`
- `TestKeccak256PreimageTracerMemoryOffset`
- `TestKeccak256PreimageTracerMemoryPadding`
- `TestKeccak256PreimageTracerDuplicateHashes`
- `TestKeccak256PreimageTracerWithExecutionError`
- `TestKeccak256PreimageTracerInsufficientStack`
- `TestKeccak256PreimageTracerLargeData`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
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

package native_test

import (
	"encoding/json"
...
```