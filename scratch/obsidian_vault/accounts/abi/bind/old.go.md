# old.go

## Architecture Metrics
- **Path:** `accounts/abi/bind/old.go`
- **Extension:** `.go`
- **Size:** 11630 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MetaData`
- `Bind`
- `NewTransactor`
- `NewKeyStoreTransactor`
- `NewKeyedTransactor`
- `NewTransactorWithChainID`
- `NewKeyStoreTransactorWithChainID`
- `NewKeyedTransactorWithChainID`
- `NewClefTransactor`
- `NewBoundContract`
- `DeployContract`
- `GetAbi`
- `WaitMined`
- `WaitMinedHash`
- `WaitDeployed`
- `WaitDeployedHash`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[accounts/abi/abigen/bind.go.md|accounts/abi/abigen/bind.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[ethclient/simulated/backend_test.go.md|ethclient/simulated/backend_test.go]]

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

// Package bind is the runtime for abigen v1 generated contract bindings.
// Deprecated: please use github.com/ethereum/go-ethereum/bind/v2
package bind

...
```