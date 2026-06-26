# api.go

## Architecture Metrics
- **Path:** `internal/ethapi/api.go`
- **Extension:** `.go`
- **Size:** 82387 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 20

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EthereumAPI`
- `feeHistoryResult`
- `TxPoolAPI`
- `EthereumAccountAPI`
- `BlockChainAPI`
- `AccountResult`
- `StorageResult`
- `ChainContextBackend`
- `ChainContext`
- `RPCTransaction`
- `accessListResult`
- `config`
- `configResponse`
- `TransactionAPI`
- `SignTransactionResult`
- `DebugAPI`
- `NetAPI`
- `NewEthereumAPI`
- `GasPrice`
- `MaxPriorityFeePerGas`
- `FeeHistory`
- `BlobBaseFee`
- `BaseFee`
- `Syncing`
- `NewTxPoolAPI`
- `flattenTxs`
- `Content`
- `ContentFrom`
- `Status`
- `Inspect`
- `NewEthereumAccountAPI`
- `Accounts`
- `NewBlockChainAPI`
- `ChainId`
- `BlockNumber`
- `blockNrOrHashOrLatest`
- `GetBalance`
- `Put`
- `Delete`
- `GetProof`
- `decodeStorageKey`
- `GetHeaderByNumber`
- `GetHeaderByHash`
- `GetBlockByNumber`
- `GetBlockByHash`
- `GetUncleByBlockNumberAndIndex`
- `GetUncleByBlockHashAndIndex`
- `GetUncleCountByBlockNumber`
- `GetUncleCountByBlockHash`
- `GetCode`
- `GetStorageAt`
- `GetStorageValues`
- `GetBlockReceipts`
- `NewChainContext`
- `Engine`
- `GetHeader`
- `Config`
- `CurrentHeader`
- `GetHeaderByNumber`
- `GetHeaderByHash`
- `doCall`
- `applyMessage`
- `applyMessageWithEVM`
- `DoCall`
- `Call`
- `SimulateV1`
- `DoEstimateGas`
- `EstimateGas`
- `RPCMarshalHeader`
- `RPCMarshalBlock`
- `newRPCTransaction`
- `effectiveGasPrice`
- `NewRPCPendingTransaction`
- `newRPCTransactionFromBlockIndex`
- `newRPCRawTransactionFromBlockIndex`
- `CreateAccessList`
- `Config`
- `AccessList`
- `NewTransactionAPI`
- `GetBlockTransactionCountByNumber`
- `GetBlockTransactionCountByHash`
- `GetTransactionByBlockNumberAndIndex`
- `GetTransactionByBlockHashAndIndex`
- `GetRawTransactionByBlockNumberAndIndex`
- `GetRawTransactionByBlockHashAndIndex`
- `GetTransactionCount`
- `GetTransactionByHash`
- `GetRawTransactionByHash`
- `GetTransactionReceipt`
- `MarshalReceipt`
- `sign`
- `SubmitTransaction`
- `SendTransaction`
- `FillTransaction`
- `currentBlobSidecarVersion`
- `SendRawTransaction`
- `SendRawTransactionSync`
- `Sign`
- `SignTransaction`
- `PendingTransactions`
- `Resend`
- `NewDebugAPI`
- `GetRawHeader`
- `GetRawBlock`
- `GetRawReceipts`
- `GetRawTransaction`
- `PrintBlock`
- `ChaindbProperty`
- `ChaindbCompact`
- `SetHead`
- `NewNetAPI`
- `Listening`
- `PeerCount`
- `Version`
- `checkTxFee`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/forkid/forkid.go.md|core/forkid/forkid.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/gasestimator/gasestimator.go.md|eth/gasestimator/gasestimator.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[log/format.go.md|log/format.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package ethapi

import (
	"context"
...
```