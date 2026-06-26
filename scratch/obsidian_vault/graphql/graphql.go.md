# graphql.go

## Architecture Metrics
- **Path:** `graphql/graphql.go`
- **Extension:** `.go`
- **Size:** 43256 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Account`
- `Log`
- `AccessTuple`
- `Withdrawal`
- `Transaction`
- `Block`
- `BlockNumberArgs`
- `BlockFilterCriteria`
- `CallData`
- `CallResult`
- `Pending`
- `Resolver`
- `FilterCriteria`
- `SyncState`
- `ImplementsGraphQLType`
- `UnmarshalGraphQL`
- `getState`
- `Address`
- `Balance`
- `TransactionCount`
- `Code`
- `Storage`
- `Transaction`
- `Account`
- `Index`
- `Topics`
- `Data`
- `Address`
- `StorageKeys`
- `Index`
- `Validator`
- `Address`
- `Amount`
- `resolve`
- `Hash`
- `InputData`
- `Gas`
- `GasPrice`
- `EffectiveGasPrice`
- `MaxFeePerGas`
- `MaxPriorityFeePerGas`
- `MaxFeePerBlobGas`
- `BlobVersionedHashes`
- `EffectiveTip`
- `Value`
- `Nonce`
- `To`
- `From`
- `Block`
- `Index`
- `getReceipt`
- `Status`
- `GasUsed`
- `CumulativeGasUsed`
- `BlobGasUsed`
- `BlobGasPrice`
- `CreatedContract`
- `Logs`
- `getLogs`
- `Type`
- `AccessList`
- `R`
- `S`
- `V`
- `YParity`
- `Raw`
- `RawReceipt`
- `resolve`
- `resolveHeader`
- `resolveReceipts`
- `Number`
- `Hash`
- `GasLimit`
- `GasUsed`
- `BaseFeePerGas`
- `NextBaseFeePerGas`
- `Parent`
- `Difficulty`
- `Timestamp`
- `Nonce`
- `MixHash`
- `TransactionsRoot`
- `StateRoot`
- `ReceiptsRoot`
- `OmmerHash`
- `OmmerCount`
- `Ommers`
- `ExtraData`
- `LogsBloom`
- `RawHeader`
- `Raw`
- `NumberOr`
- `NumberOrLatest`
- `Miner`
- `TransactionCount`
- `Transactions`
- `TransactionAt`
- `OmmerAt`
- `WithdrawalsRoot`
- `Withdrawals`
- `BlobGasUsed`
- `ExcessBlobGas`
- `SlotNumber`
- `runFilter`
- `Logs`
- `Account`
- `Data`
- `GasUsed`
- `Status`
- `Call`
- `EstimateGas`
- `TransactionCount`
- `Transactions`
- `Account`
- `Call`
- `EstimateGas`
- `Block`
- `Blocks`
- `Pending`
- `Transaction`
- `SendRawTransaction`
- `Logs`
- `GasPrice`
- `MaxPriorityFeePerGas`
- `ChainID`
- `StartingBlock`
- `CurrentBlock`
- `HighestBlock`
- `SyncedAccounts`
- `SyncedAccountBytes`
- `SyncedBytecodes`
- `SyncedBytecodeBytes`
- `SyncedStorage`
- `SyncedStorageBytes`
- `HealedTrienodes`
- `HealedTrienodeBytes`
- `HealedBytecodes`
- `HealedBytecodeBytes`
- `HealingTrienodes`
- `HealingBytecode`
- `TxIndexFinishedBlocks`
- `TxIndexRemainingBlocks`
- `StateIndexRemaining`
- `TrienodeIndexRemaining`
- `Syncing`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

// Package graphql provides a GraphQL interface to Ethereum node data.
package graphql

import (
...
```