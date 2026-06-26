# api_benchmark_test.go

## Architecture Metrics
- **Path:** `eth/catalyst/api_benchmark_test.go`
- **Extension:** `.go`
- **Size:** 24936 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `benchmarkBlobEnv`
- `discardConn`
- `String`
- `benchEncode`
- `init`
- `makeBenchBlobTx`
- `newBenchmarkBlobEnv`
- `addBlobTxs`
- `Close`
- `BenchmarkGetBlobsV1`
- `BenchmarkGetBlobsV2Extended`
- `BenchmarkGetBlobsV3`
- `BenchmarkGetPayloadV5WithBlobs`
- `BenchmarkNewPayloadV3WithBlobs`
- `BenchmarkForkchoiceUpdatedWithBlobPayload`
- `BenchmarkFullBlobWorkflowOsaka`
- `Close`
- `SetWriteDeadline`
- `BenchmarkGetPayloadV5RPCServerOnly`
- `BenchmarkGetBlobsV3RPCServerOnly`

## Imports (Dependencies)
- [[beacon/engine/bapl_encode.go.md|beacon/engine/bapl_encode.go]]
- [[common/big.go.md|common/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

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
package catalyst

import (
	"context"
	"crypto/ecdsa"
...
```