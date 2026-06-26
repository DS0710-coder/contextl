# block.go

## Architecture Metrics
- **Path:** `cmd/evm/internal/t8ntool/block.go`
- **Extension:** `.go`
- **Size:** 11675 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `header`
- `headerMarshaling`
- `bbInput`
- `cliqueInput`
- `extblock`
- `blockInfo`
- `UnmarshalJSON`
- `ToBlock`
- `SealBlock`
- `sealClique`
- `BuildBlock`
- `readInput`
- `dispatchBlock`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/evm/t8n_test.go.md|cmd/evm/t8n_test.go]]

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package t8ntool

import (
	"crypto/ecdsa"
...
```