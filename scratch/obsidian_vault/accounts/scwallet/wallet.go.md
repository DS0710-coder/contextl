# wallet.go

## Architecture Metrics
- **Path:** `accounts/scwallet/wallet.go`
- **Extension:** `.go`
- **Size:** 35897 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Wallet`
- `applicationInfo`
- `Session`
- `walletStatus`
- `initializeData`
- `keyExport`
- `signatureData`
- `NewWallet`
- `transmit`
- `connect`
- `doselect`
- `ping`
- `release`
- `pair`
- `Unpair`
- `URL`
- `Status`
- `Open`
- `Close`
- `selfDerive`
- `Accounts`
- `makeAccount`
- `Contains`
- `Initialize`
- `Derive`
- `SelfDerive`
- `SignData`
- `signHash`
- `SignTx`
- `SignDataWithPassphrase`
- `signHashWithPassphrase`
- `SignText`
- `SignTextWithPassphrase`
- `SignTxWithPassphrase`
- `findAccountPath`
- `pair`
- `unpair`
- `verifyPin`
- `unblockPin`
- `release`
- `paired`
- `authenticate`
- `walletStatus`
- `derivationPath`
- `initialize`
- `derive`
- `publicKey`
- `sign`
- `confirmPublicKey`
- `makeRecoverableSignature`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

package scwallet

import (
	"bytes"
...
```