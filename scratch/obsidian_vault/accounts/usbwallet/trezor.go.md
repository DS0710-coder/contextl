# trezor.go

## Architecture Metrics
- **Path:** `accounts/usbwallet/trezor.go`
- **Extension:** `.go`
- **Size:** 14720 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `trezorDriver`
- `newTrezorDriver`
- `Status`
- `Open`
- `Close`
- `Heartbeat`
- `Derive`
- `SignTx`
- `SignTypedMessage`
- `trezorDerive`
- `trezorSign`
- `trezorExchange`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/usbwallet/trezor.go.md|accounts/usbwallet/trezor.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[accounts/usbwallet/trezor.go.md|accounts/usbwallet/trezor.go]]

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

// This file contains the implementation for interacting with the Trezor hardware
// wallets. The wire protocol spec can be found on the SatoshiLabs website:
// https://doc.satoshilabs.com/trezor-tech/api-protobuf.html

...
```