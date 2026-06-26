# gethclient_test.go

## Architecture Metrics
- **Path:** `ethclient/gethclient/gethclient_test.go`
- **Extension:** `.go`
- **Size:** 20235 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `newTestBackend`
- `generateTestChain`
- `TestGethClient`
- `testAccessList`
- `testGetProof`
- `testGetProofCanonicalizeKeys`
- `testGetProofNonExistent`
- `testGCStats`
- `testMemStats`
- `testGetNodeInfo`
- `testSetHead`
- `testSubscribePendingTransactions`
- `testCallContract`
- `testTraceTransactions`
- `TestOverrideAccountMarshal`
- `TestBlockOverridesMarshal`
- `testCallContractWithBlockOverrides`
- `testTraceTransactionWithCallTracer`
- `testTraceCallWithCallTracer`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/native/4byte.go.md|eth/tracers/native/4byte.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

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

package gethclient

import (
	"bytes"
...
```