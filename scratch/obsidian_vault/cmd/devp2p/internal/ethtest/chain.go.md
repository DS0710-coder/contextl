# chain.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/ethtest/chain.go`
- **Extension:** `.go`
- **Size:** 9542 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Chain`
- `txInfo`
- `senderInfo`
- `account`
- `NewChain`
- `Head`
- `AccountsInHashOrder`
- `CodeHashes`
- `Len`
- `ForkID`
- `TD`
- `GetBlock`
- `RootAt`
- `GetSender`
- `IncNonce`
- `Balance`
- `SignTx`
- `GetHeaders`
- `Shorten`
- `loadGenesis`
- `blocksFromFile`
- `readState`
- `readAccounts`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/forkid/forkid.go.md|core/forkid/forkid.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package ethtest

import (
	"bytes"
...
```