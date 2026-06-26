# transaction_signing.go

## Architecture Metrics
- **Path:** `core/types/transaction_signing.go`
- **Extension:** `.go`
- **Size:** 16153 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `sigCache`
- `Signer`
- `modernSigner`
- `EIP155Signer`
- `HomesteadSigner`
- `FrontierSigner`
- `MakeSigner`
- `LatestSigner`
- `LatestSignerForChainID`
- `SignTx`
- `SignNewTx`
- `MustSignNewTx`
- `Sender`
- `set`
- `has`
- `newModernSigner`
- `ChainID`
- `Equal`
- `Hash`
- `supportsType`
- `Sender`
- `SignatureValues`
- `NewPragueSigner`
- `NewCancunSigner`
- `NewLondonSigner`
- `NewEIP2930Signer`
- `NewEIP155Signer`
- `ChainID`
- `Equal`
- `Sender`
- `SignatureValues`
- `Hash`
- `ChainID`
- `Equal`
- `SignatureValues`
- `Sender`
- `ChainID`
- `Equal`
- `Sender`
- `SignatureValues`
- `Hash`
- `decodeSignature`
- `recoverPlain`
- `deriveChainId`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[params/forks/forks.go.md|params/forks/forks.go]]

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

package types

import (
	"crypto/ecdsa"
...
```