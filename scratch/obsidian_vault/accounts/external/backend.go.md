# backend.go

## Architecture Metrics
- **Path:** `accounts/external/backend.go`
- **Extension:** `.go`
- **Size:** 8943 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ExternalBackend`
- `ExternalSigner`
- `signTransactionResult`
- `Wallets`
- `NewExternalBackend`
- `Subscribe`
- `NewExternalSigner`
- `URL`
- `Status`
- `Open`
- `Close`
- `Accounts`
- `Contains`
- `Derive`
- `SelfDerive`
- `SignData`
- `SignText`
- `SignTx`
- `SignTextWithPassphrase`
- `SignTxWithPassphrase`
- `SignDataWithPassphrase`
- `listAccounts`
- `pingVersion`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[rpc/client.go.md|rpc/client.go]]
- [[signer/core/apitypes/signed_data_internal_test.go.md|signer/core/apitypes/signed_data_internal_test.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]

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

package external

import (
	"errors"
...
```