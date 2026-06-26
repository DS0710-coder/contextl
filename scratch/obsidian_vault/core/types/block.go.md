# block.go

## Architecture Metrics
- **Path:** `core/types/block.go`
- **Extension:** `.go`
- **Size:** 18888 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Header`
- `headerMarshaling`
- `Body`
- `Block`
- `extblock`
- `EncodeNonce`
- `Uint64`
- `MarshalText`
- `UnmarshalText`
- `Hash`
- `Size`
- `SanityCheck`
- `EmptyBody`
- `EmptyReceipts`
- `NewBlock`
- `CopyHeader`
- `DecodeRLP`
- `EncodeRLP`
- `Body`
- `Uncles`
- `Transactions`
- `Withdrawals`
- `AccessList`
- `Transaction`
- `Header`
- `Number`
- `GasLimit`
- `GasUsed`
- `Difficulty`
- `Time`
- `NumberU64`
- `MixDigest`
- `Nonce`
- `Bloom`
- `Coinbase`
- `Root`
- `ParentHash`
- `TxHash`
- `ReceiptHash`
- `UncleHash`
- `Extra`
- `BaseFee`
- `BeaconRoot`
- `RequestsHash`
- `BlockAccessListHash`
- `ExcessBlobGas`
- `BlobGasUsed`
- `SlotNumber`
- `Size`
- `SanityCheck`
- `Write`
- `CalcUncleHash`
- `CalcRequestsHash`
- `NewBlockWithHeader`
- `WithSeal`
- `WithBody`
- `WithAccessList`
- `WithAccessListUnsafe`
- `Hash`
- `HeaderParentHashFromRLP`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

// Package types contains data types related to Ethereum consensus.
package types

import (
...
```