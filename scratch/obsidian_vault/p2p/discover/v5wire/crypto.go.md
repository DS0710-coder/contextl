# crypto.go

## Architecture Metrics
- **Path:** `p2p/discover/v5wire/crypto.go`
- **Extension:** `.go`
- **Size:** 5624 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EncodePubkey`
- `DecodePubkey`
- `idNonceHash`
- `makeIDSignature`
- `ENRKey`
- `verifyIDSignature`
- `deriveKeys`
- `ecdh`
- `encryptGCM`
- `decryptGCM`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[node/api.go.md|node/api.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/v5test/discv5tests.go.md|cmd/devp2p/internal/v5test/discv5tests.go]]
- [[cmd/devp2p/internal/v5test/framework.go.md|cmd/devp2p/internal/v5test/framework.go]]
- [[p2p/discover/v5_talk.go.md|p2p/discover/v5_talk.go]]
- [[p2p/discover/v5_udp.go.md|p2p/discover/v5_udp.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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

package v5wire

import (
	"crypto/aes"
...
```