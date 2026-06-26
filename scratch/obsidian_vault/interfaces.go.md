# interfaces.go

## Architecture Metrics
- **Path:** `interfaces.go`
- **Extension:** `.go`
- **Size:** 17953 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Subscription`
- `ChainReader`
- `TransactionReceiptsQuery`
- `TransactionReader`
- `ChainStateReader`
- `SyncProgress`
- `ChainSyncReader`
- `CallMsg`
- `ContractCaller`
- `FilterQuery`
- `LogFilterer`
- `TransactionSender`
- `GasPricer`
- `GasPricer1559`
- `FeeHistoryReader`
- `FeeHistory`
- `PendingStateReader`
- `PendingContractCaller`
- `GasEstimator`
- `PendingStateEventer`
- `BlockNumberReader`
- `ChainIDReader`
- `OverrideAccount`
- `acc`
- `BlockOverrides`
- `override`
- `Done`
- `MarshalJSON`
- `MarshalJSON`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]

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

// Package ethereum defines interfaces for interacting with Ethereum.
package ethereum

import (
...
```