# accounts.go

## Architecture Metrics
- **Path:** `accounts/accounts.go`
- **Extension:** `.go`
- **Size:** 10413 bytes
- **Centrality Score:** 0.0021
- **In-Degree (Imported By):** 30
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Account`
- `Wallet`
- `Backend`
- `WalletEvent`
- `TextHash`
- `TextAndHash`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]
- [[event/event.go.md|event/event.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/keystore/account_cache.go.md|accounts/keystore/account_cache.go]]
- [[accounts/keystore/account_cache_test.go.md|accounts/keystore/account_cache_test.go]]
- [[accounts/keystore/key.go.md|accounts/keystore/key.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[accounts/keystore/keystore_test.go.md|accounts/keystore/keystore_test.go]]
- [[accounts/keystore/passphrase.go.md|accounts/keystore/passphrase.go]]
- [[accounts/keystore/presale.go.md|accounts/keystore/presale.go]]
- [[accounts/keystore/wallet.go.md|accounts/keystore/wallet.go]]
- [[accounts/scwallet/hub.go.md|accounts/scwallet/hub.go]]
- [[accounts/scwallet/wallet.go.md|accounts/scwallet/wallet.go]]
- [[accounts/usbwallet/hub.go.md|accounts/usbwallet/hub.go]]
- [[accounts/usbwallet/ledger.go.md|accounts/usbwallet/ledger.go]]
- [[accounts/usbwallet/trezor.go.md|accounts/usbwallet/trezor.go]]
- [[accounts/usbwallet/wallet.go.md|accounts/usbwallet/wallet.go]]
- [[cmd/ethkey/message.go.md|cmd/ethkey/message.go]]
- [[cmd/geth/accountcmd.go.md|cmd/geth/accountcmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[node/node.go.md|node/node.go]]
- [[signer/core/apitypes/types.go.md|signer/core/apitypes/types.go]]

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

// Package accounts implements high level Ethereum account management.
package accounts

import (
...
```