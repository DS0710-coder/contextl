# ethclient_test.go

## Architecture Metrics
- **Path:** `ethclient/ethclient_test.go`
- **Extension:** `.go`
- **Size:** 29784 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `blockReceiptsTestService`
- `newTestBackend`
- `generateTestChain`
- `TestEthClient`
- `testHeader`
- `testBalanceAt`
- `testTransactionInBlock`
- `testChainID`
- `testGetBlock`
- `testStatusFunctions`
- `testCallContractAtHash`
- `testCallContract`
- `testAtFunctions`
- `testTransactionSender`
- `TestBlockReceiptsPreservesCanonicalFlag`
- `GetBlockReceipts`
- `newCanceledContext`
- `sendTransaction`
- `ExampleRevertErrorData`
- `TestSimulateV1`
- `TestSimulateV1WithBlockOverrides`
- `TestSimulateV1WithStateOverrides`
- `TestSimulateV1WithBlockNumberOrHash`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[common/big.go.md|common/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package ethclient_test

import (
	"bytes"
...
```