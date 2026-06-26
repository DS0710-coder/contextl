# ethclient.go

## Architecture Metrics
- **Path:** `ethclient/ethclient.go`
- **Extension:** `.go`
- **Size:** 34933 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Client`
- `rpcBlock`
- `rpcTransaction`
- `txExtraInfo`
- `feeHistoryResultMarshaling`
- `rpcProgress`
- `SimulateOptions`
- `SimulateBlock`
- `Alias`
- `SimulateCallResult`
- `simulateCallResultMarshaling`
- `CallError`
- `SimulateBlockResult`
- `simulateBlockResultMarshaling`
- `Dial`
- `DialContext`
- `NewClient`
- `Close`
- `Client`
- `ChainID`
- `BlockByHash`
- `BlockByNumber`
- `BlockNumber`
- `PeerCount`
- `BlockReceipts`
- `getBlock`
- `HeaderByHash`
- `HeaderByNumber`
- `UnmarshalJSON`
- `TransactionByHash`
- `TransactionSender`
- `TransactionCount`
- `TransactionInBlock`
- `TransactionReceipt`
- `SubscribeTransactionReceipts`
- `SyncProgress`
- `SubscribeNewHead`
- `NetworkID`
- `BalanceAt`
- `BalanceAtHash`
- `StorageAt`
- `StorageAtHash`
- `CodeAt`
- `CodeAtHash`
- `NonceAt`
- `NonceAtHash`
- `FilterLogs`
- `SubscribeFilterLogs`
- `toFilterArg`
- `PendingBalanceAt`
- `PendingStorageAt`
- `PendingCodeAt`
- `PendingNonceAt`
- `PendingTransactionCount`
- `CallContract`
- `CallContractAtHash`
- `PendingCallContract`
- `SuggestGasPrice`
- `SuggestGasTipCap`
- `BlobBaseFee`
- `FeeHistory`
- `EstimateGas`
- `EstimateGasAtBlock`
- `EstimateGasAtBlockHash`
- `SendTransaction`
- `SendTransactionSync`
- `SendRawTransactionSync`
- `RevertErrorData`
- `toBlockNumArg`
- `toCallArg`
- `toSyncProgress`
- `MarshalJSON`
- `SimulateV1`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[cmd/fetchpayload/main.go.md|cmd/fetchpayload/main.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/workload/client.go.md|cmd/workload/client.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]

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

// Package ethclient provides a client for the Ethereum RPC API.
package ethclient

import (
...
```