# api_test.go

## Architecture Metrics
- **Path:** `internal/ethapi/api_test.go`
- **Extension:** `.go`
- **Size:** 142209 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 22

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `txData`
- `testBackend`
- `log`
- `callErr`
- `callRes`
- `blockRes`
- `resultType`
- `result`
- `account`
- `configTimeBackend`
- `testTransactionMarshal`
- `TestTransaction_RoundTripRpcJSON`
- `TestTransactionBlobTx`
- `allTransactionTypes`
- `allBlobTxs`
- `newTestAccountManager`
- `fakeBlockHash`
- `newTestBackend`
- `SyncProgress`
- `SuggestGasTipCap`
- `FeeHistory`
- `BlobBaseFee`
- `BaseFee`
- `ChainDb`
- `AccountManager`
- `ExtRPCEnabled`
- `RPCGasCap`
- `RPCEVMTimeout`
- `RPCTxFeeCap`
- `UnprotectedAllowed`
- `SetHead`
- `HeaderByNumber`
- `HeaderByHash`
- `HeaderByNumberOrHash`
- `CurrentHeader`
- `CurrentBlock`
- `BlockByNumber`
- `BlockByHash`
- `BlockByNumberOrHash`
- `GetBody`
- `StateAndHeaderByNumber`
- `StateAndHeaderByNumberOrHash`
- `Pending`
- `GetReceipts`
- `GetEVM`
- `SubscribeChainEvent`
- `SubscribeChainHeadEvent`
- `SendTx`
- `GetCanonicalTransaction`
- `GetCanonicalReceipt`
- `TxIndexDone`
- `GetPoolTransactions`
- `GetPoolTransaction`
- `GetPoolNonce`
- `Stats`
- `TxPoolContent`
- `TxPoolContentFrom`
- `SubscribeNewTxsEvent`
- `ChainConfig`
- `Engine`
- `GetLogs`
- `SubscribeRemovedLogsEvent`
- `SubscribeLogsEvent`
- `CurrentView`
- `NewMatcherBackend`
- `HistoryPruningCutoff`
- `HistoryRetention`
- `TestEstimateGas`
- `TestCall`
- `TestSimulateV1`
- `TestSimulateV1ChainLinkage`
- `TestSimulateV1TxSender`
- `TestSimulateV1WithdrawalsByFork`
- `TestSignTransaction`
- `TestSignBlobTransaction`
- `TestSendBlobTransaction`
- `TestFillBlobTransaction`
- `testFillBlobTransaction`
- `argsFromTransaction`
- `newAccounts`
- `newTestAccount`
- `newRPCBalance`
- `hex2Bytes`
- `newUint64`
- `newBytes`
- `uint256ToBytes`
- `TestRPCMarshalBlock`
- `TestRPCGetBlockOrHeader`
- `setupReceiptBackend`
- `TestRPCGetTransactionReceipt`
- `TestRPCGetBlockReceipts`
- `testRPCResponseWithFile`
- `addressToHash`
- `TestCreateAccessListWithStateOverrides`
- `TestEstimateGasWithMovePrecompile`
- `TestEIP7910Config`
- `ChainConfig`
- `HeaderByNumber`
- `CurrentHeader`
- `RPCTxSyncDefaultTimeout`
- `RPCTxSyncMaxTimeout`
- `RPCTxSyncDefaultTimeout`
- `RPCTxSyncMaxTimeout`
- `makeSignedRaw`
- `makeSelfSignedRaw`
- `TestSendRawTransactionSync_Success`
- `TestSendRawTransactionSync_Timeout`
- `TestGetStorageValues`
- `TestStateMethodsDefaultToLatest`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/blocktest/test_hash.go.md|internal/blocktest/test_hash.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

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

package ethapi

import (
	"bytes"
...
```