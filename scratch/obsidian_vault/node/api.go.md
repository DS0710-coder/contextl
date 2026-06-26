# api.go

## Architecture Metrics
- **Path:** `node/api.go`
- **Extension:** `.go`
- **Size:** 9938 bytes
- **Centrality Score:** 0.0065
- **In-Degree (Imported By):** 105
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `adminAPI`
- `web3API`
- `p2pDebugAPI`
- `apis`
- `AddPeer`
- `RemovePeer`
- `AddTrustedPeer`
- `RemoveTrustedPeer`
- `PeerEvents`
- `StartHTTP`
- `StartRPC`
- `StopHTTP`
- `StopRPC`
- `StartWS`
- `StopWS`
- `Peers`
- `NodeInfo`
- `Datadir`
- `ClientVersion`
- `Sha3`
- `DiscoveryV4Table`

## Imports (Dependencies)
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/devp2p/crawl.go.md|cmd/devp2p/crawl.go]]
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/devp2p/dnscmd.go.md|cmd/devp2p/dnscmd.go]]
- [[cmd/devp2p/enrcmd.go.md|cmd/devp2p/enrcmd.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/devp2p/internal/v4test/discv4tests.go.md|cmd/devp2p/internal/v4test/discv4tests.go]]
- [[cmd/devp2p/internal/v4test/framework.go.md|cmd/devp2p/internal/v4test/framework.go]]
- [[cmd/devp2p/internal/v5test/discv5tests.go.md|cmd/devp2p/internal/v5test/discv5tests.go]]
- [[cmd/devp2p/internal/v5test/framework.go.md|cmd/devp2p/internal/v5test/framework.go]]
- [[cmd/devp2p/keycmd.go.md|cmd/devp2p/keycmd.go]]
- [[cmd/devp2p/main.go.md|cmd/devp2p/main.go]]
- [[cmd/devp2p/nodeset.go.md|cmd/devp2p/nodeset.go]]
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/state_object.go.md|core/state/state_object.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/stateupdate.go.md|core/state/stateupdate.go]]
- [[core/tracing/hooks.go.md|core/tracing/hooks.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth.go.md|eth/handler_eth.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_snap.go.md|eth/handler_snap.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/discovery.go.md|eth/protocols/eth/discovery.go]]
- [[eth/protocols/eth/handler.go.md|eth/protocols/eth/handler.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handshake_test.go.md|eth/protocols/eth/handshake_test.go]]
- [[eth/protocols/eth/peer_test.go.md|eth/protocols/eth/peer_test.go]]
- [[eth/protocols/snap/handler.go.md|eth/protocols/snap/handler.go]]
- [[eth/protocols/snap/handler_fuzzing_test.go.md|eth/protocols/snap/handler_fuzzing_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/sync_test.go.md|eth/sync_test.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/config_toml.go.md|p2p/config_toml.go]]
- [[p2p/dial.go.md|p2p/dial.go]]
- [[p2p/dial_test.go.md|p2p/dial_test.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]
- [[p2p/discover/lookup.go.md|p2p/discover/lookup.go]]
- [[p2p/discover/node.go.md|p2p/discover/node.go]]
- [[p2p/discover/table.go.md|p2p/discover/table.go]]
- [[p2p/discover/table_reval.go.md|p2p/discover/table_reval.go]]
- [[p2p/discover/table_reval_test.go.md|p2p/discover/table_reval_test.go]]
- [[p2p/discover/table_test.go.md|p2p/discover/table_test.go]]
- [[p2p/discover/table_util_test.go.md|p2p/discover/table_util_test.go]]
- [[p2p/discover/v4_lookup_test.go.md|p2p/discover/v4_lookup_test.go]]
- [[p2p/discover/v4_udp.go.md|p2p/discover/v4_udp.go]]
- [[p2p/discover/v4_udp_test.go.md|p2p/discover/v4_udp_test.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v5_talk.go.md|p2p/discover/v5_talk.go]]
- [[p2p/discover/v5_udp.go.md|p2p/discover/v5_udp.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/discover/v5wire/crypto_test.go.md|p2p/discover/v5wire/crypto_test.go]]
- [[p2p/discover/v5wire/encoding.go.md|p2p/discover/v5wire/encoding.go]]
- [[p2p/discover/v5wire/encoding_test.go.md|p2p/discover/v5wire/encoding_test.go]]
- [[p2p/discover/v5wire/msg.go.md|p2p/discover/v5wire/msg.go]]
- [[p2p/discover/v5wire/session.go.md|p2p/discover/v5wire/session.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/dnsdisc/sync.go.md|p2p/dnsdisc/sync.go]]
- [[p2p/dnsdisc/tree.go.md|p2p/dnsdisc/tree.go]]
- [[p2p/dnsdisc/tree_test.go.md|p2p/dnsdisc/tree_test.go]]
- [[p2p/message.go.md|p2p/message.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/peer_test.go.md|p2p/peer_test.go]]
- [[p2p/protocol.go.md|p2p/protocol.go]]
- [[p2p/server.go.md|p2p/server.go]]
- [[p2p/server_test.go.md|p2p/server_test.go]]
- [[trie/bintrie/format_test.go.md|trie/bintrie/format_test.go]]
- [[trie/bintrie/trie.go.md|trie/bintrie/trie.go]]
- [[trie/committer.go.md|trie/committer.go]]
- [[trie/database_test.go.md|trie/database_test.go]]
- [[trie/inspect_test.go.md|trie/inspect_test.go]]
- [[trie/iterator_test.go.md|trie/iterator_test.go]]
- [[trie/secure_trie.go.md|trie/secure_trie.go]]
- [[trie/secure_trie_test.go.md|trie/secure_trie_test.go]]
- [[trie/stacktrie_fuzzer_test.go.md|trie/stacktrie_fuzzer_test.go]]
- [[trie/sync_test.go.md|trie/sync_test.go]]
- [[trie/tracer_test.go.md|trie/tracer_test.go]]
- [[trie/transitiontrie/transition.go.md|trie/transitiontrie/transition.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]
- [[triedb/pathdb/database.go.md|triedb/pathdb/database.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/difflayer_test.go.md|triedb/pathdb/difflayer_test.go]]
- [[triedb/pathdb/execute.go.md|triedb/pathdb/execute.go]]
- [[triedb/pathdb/flush.go.md|triedb/pathdb/flush.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/iterator_test.go.md|triedb/pathdb/iterator_test.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/nodes_test.go.md|triedb/pathdb/nodes_test.go]]

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package node

import (
	"context"
...
```