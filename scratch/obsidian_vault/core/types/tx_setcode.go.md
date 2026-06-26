# tx_setcode.go

## Architecture Metrics
- **Path:** `core/types/tx_setcode.go`
- **Extension:** `.go`
- **Size:** 7439 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SetCodeTx`
- `SetCodeAuthorization`
- `authorizationMarshaling`
- `ParseDelegation`
- `AddressToDelegation`
- `SignSetCode`
- `SigHash`
- `Authority`
- `copy`
- `txType`
- `chainID`
- `accessList`
- `data`
- `gas`
- `gasFeeCap`
- `gasTipCap`
- `gasPrice`
- `value`
- `nonce`
- `to`
- `effectiveGasPrice`
- `rawSignatureValues`
- `setSignatureValues`
- `encode`
- `decode`
- `sigHash`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package types

import (
	"bytes"
...
```