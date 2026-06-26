# keystore.go

## Architecture Metrics
- **Path:** `accounts/keystore/keystore.go`
- **Extension:** `.go`
- **Size:** 16934 bytes
- **Centrality Score:** 0.0013
- **In-Degree (Imported By):** 12
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `KeyStore`
- `unlocked`
- `NewKeyStore`
- `init`
- `Wallets`
- `refreshWallets`
- `Subscribe`
- `updater`
- `HasAddress`
- `Accounts`
- `Delete`
- `SignHash`
- `SignTx`
- `SignHashWithPassphrase`
- `SignTxWithPassphrase`
- `Unlock`
- `Lock`
- `TimedUnlock`
- `Find`
- `getDecryptedKey`
- `expire`
- `NewAccount`
- `Export`
- `Import`
- `ImportECDSA`
- `importKey`
- `Update`
- `ImportPreSaleKey`
- `isUpdating`
- `zeroKey`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[event/event.go.md|event/event.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/devp2p/dnscmd.go.md|cmd/devp2p/dnscmd.go]]
- [[cmd/ethkey/changepassword.go.md|cmd/ethkey/changepassword.go]]
- [[cmd/ethkey/generate.go.md|cmd/ethkey/generate.go]]
- [[cmd/ethkey/inspect.go.md|cmd/ethkey/inspect.go]]
- [[cmd/ethkey/message.go.md|cmd/ethkey/message.go]]
- [[cmd/geth/accountcmd.go.md|cmd/geth/accountcmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/guide/guide_test.go.md|internal/guide/guide_test.go]]

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

// Package keystore implements encrypted storage of secp256k1 private keys.
//
// Keys are stored as encrypted JSON files according to the Web3 Secret Storage specification.
// See https://ethereum.org/en/developers/docs/data-structures-and-encoding/web3-secret-storage/ for more information.
...
```