# enr.go

## Architecture Metrics
- **Path:** `p2p/enr/enr.go`
- **Extension:** `.go`
- **Size:** 9515 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 38
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `IdentityScheme`
- `Record`
- `pair`
- `Verify`
- `NodeAddr`
- `Size`
- `computeSize`
- `Seq`
- `SetSeq`
- `Load`
- `Set`
- `invalidate`
- `Signature`
- `EncodeRLP`
- `DecodeRLP`
- `decodeRecord`
- `IdentityScheme`
- `VerifySignature`
- `SetSig`
- `AppendElements`
- `encode`

## Imports (Dependencies)
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/enrcmd.go.md|cmd/devp2p/enrcmd.go]]
- [[cmd/devp2p/internal/v5test/framework.go.md|cmd/devp2p/internal/v5test/framework.go]]
- [[cmd/devp2p/keycmd.go.md|cmd/devp2p/keycmd.go]]
- [[cmd/devp2p/nodesetcmd.go.md|cmd/devp2p/nodesetcmd.go]]
- [[eth/protocols/eth/handler.go.md|eth/protocols/eth/handler.go]]
- [[eth/protocols/snap/handler.go.md|eth/protocols/snap/handler.go]]
- [[p2p/dial.go.md|p2p/dial.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]
- [[p2p/discover/table.go.md|p2p/discover/table.go]]
- [[p2p/discover/table_reval_test.go.md|p2p/discover/table_reval_test.go]]
- [[p2p/discover/table_test.go.md|p2p/discover/table_test.go]]
- [[p2p/discover/table_util_test.go.md|p2p/discover/table_util_test.go]]
- [[p2p/discover/v4_lookup_test.go.md|p2p/discover/v4_lookup_test.go]]
- [[p2p/discover/v4_udp_test.go.md|p2p/discover/v4_udp_test.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v5_udp.go.md|p2p/discover/v5_udp.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]
- [[p2p/discover/v5wire/encoding.go.md|p2p/discover/v5wire/encoding.go]]
- [[p2p/discover/v5wire/msg.go.md|p2p/discover/v5wire/msg.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/dnsdisc/tree.go.md|p2p/dnsdisc/tree.go]]
- [[p2p/enode/idscheme.go.md|p2p/enode/idscheme.go]]
- [[p2p/enode/idscheme_test.go.md|p2p/enode/idscheme_test.go]]
- [[p2p/enode/iter_test.go.md|p2p/enode/iter_test.go]]
- [[p2p/enode/localnode.go.md|p2p/enode/localnode.go]]
- [[p2p/enode/localnode_test.go.md|p2p/enode/localnode_test.go]]
- [[p2p/enode/node.go.md|p2p/enode/node.go]]
- [[p2p/enode/node_test.go.md|p2p/enode/node_test.go]]
- [[p2p/enode/nodedb.go.md|p2p/enode/nodedb.go]]
- [[p2p/enode/urlv4.go.md|p2p/enode/urlv4.go]]
- [[p2p/enode/urlv4_test.go.md|p2p/enode/urlv4_test.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/peer_test.go.md|p2p/peer_test.go]]
- [[p2p/protocol.go.md|p2p/protocol.go]]
- [[p2p/server.go.md|p2p/server.go]]
- [[p2p/server_nat.go.md|p2p/server_nat.go]]
- [[p2p/server_test.go.md|p2p/server_test.go]]

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

// Package enr implements Ethereum Node Records as defined in EIP-778. A node record holds
// arbitrary information about a node on the peer-to-peer network. Node information is
// stored in key/value pairs. To store and retrieve key/values in a record, use the Entry
// interface.
...
```