# rlpx.go

## Architecture Metrics
- **Path:** `p2p/rlpx/rlpx.go`
- **Extension:** `.go`
- **Size:** 19401 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Conn`
- `sessionState`
- `hashMAC`
- `Secrets`
- `handshakeState`
- `authMsgV4`
- `authRespV4`
- `newHashMAC`
- `NewConn`
- `SetSnappy`
- `SetReadDeadline`
- `SetWriteDeadline`
- `SetDeadline`
- `Read`
- `readFrame`
- `Write`
- `writeFrame`
- `computeHeader`
- `computeFrame`
- `compute`
- `Handshake`
- `InitWithSecrets`
- `Close`
- `runRecipient`
- `handleAuthMsg`
- `secrets`
- `staticSharedSecret`
- `runInitiator`
- `makeAuthMsg`
- `handleAuthResp`
- `makeAuthResp`
- `readMsg`
- `sealEIP8`
- `importPublicKey`
- `exportPubkey`
- `xor`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/ecies/ecies.go.md|crypto/ecies/ecies.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/conn.go.md|cmd/devp2p/internal/ethtest/conn.go]]
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]
- [[p2p/server_test.go.md|p2p/server_test.go]]
- [[p2p/transport.go.md|p2p/transport.go]]

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

// Package rlpx implements the RLPx transport protocol.
package rlpx

import (
...
```