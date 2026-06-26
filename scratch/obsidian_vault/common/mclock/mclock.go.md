# mclock.go

## Architecture Metrics
- **Path:** `common/mclock/mclock.go`
- **Extension:** `.go`
- **Size:** 3465 bytes
- **Centrality Score:** 0.0034
- **In-Degree (Imported By):** 43
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Clock`
- `Timer`
- `ChanTimer`
- `System`
- `systemTimer`
- `nanotime`
- `Now`
- `Add`
- `Sub`
- `Now`
- `Sleep`
- `NewTimer`
- `After`
- `AfterFunc`
- `Reset`
- `C`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[beacon/light/committee_chain_test.go.md|beacon/light/committee_chain_test.go]]
- [[beacon/light/request/server.go.md|beacon/light/request/server.go]]
- [[beacon/light/request/server_test.go.md|beacon/light/request/server_test.go]]
- [[cmd/devp2p/internal/v5test/framework.go.md|cmd/devp2p/internal/v5test/framework.go]]
- [[common/prque/lazyqueue.go.md|common/prque/lazyqueue.go]]
- [[common/prque/lazyqueue_test.go.md|common/prque/lazyqueue_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_insert.go.md|core/blockchain_insert.go]]
- [[core/filtermaps/matcher.go.md|core/filtermaps/matcher.go]]
- [[core/txpool/blobpool/cache.go.md|core/txpool/blobpool/cache.go]]
- [[core/txpool/blobpool/cache_test.go.md|core/txpool/blobpool/cache_test.go]]
- [[eth/dropper.go.md|eth/dropper.go]]
- [[eth/fetcher/tx_fetcher.go.md|eth/fetcher/tx_fetcher.go]]
- [[eth/fetcher/tx_fetcher_test.go.md|eth/fetcher/tx_fetcher_test.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[event/subscription.go.md|event/subscription.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/dial.go.md|p2p/dial.go]]
- [[p2p/dial_test.go.md|p2p/dial_test.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]
- [[p2p/discover/table.go.md|p2p/discover/table.go]]
- [[p2p/discover/table_reval.go.md|p2p/discover/table_reval.go]]
- [[p2p/discover/table_reval_test.go.md|p2p/discover/table_reval_test.go]]
- [[p2p/discover/table_test.go.md|p2p/discover/table_test.go]]
- [[p2p/discover/v5_udp.go.md|p2p/discover/v5_udp.go]]
- [[p2p/discover/v5wire/encoding.go.md|p2p/discover/v5wire/encoding.go]]
- [[p2p/discover/v5wire/encoding_test.go.md|p2p/discover/v5wire/encoding_test.go]]
- [[p2p/discover/v5wire/msg.go.md|p2p/discover/v5wire/msg.go]]
- [[p2p/discover/v5wire/session.go.md|p2p/discover/v5wire/session.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/dnsdisc/sync.go.md|p2p/dnsdisc/sync.go]]
- [[p2p/netutil/iptrack.go.md|p2p/netutil/iptrack.go]]
- [[p2p/netutil/iptrack_test.go.md|p2p/netutil/iptrack_test.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/server.go.md|p2p/server.go]]
- [[p2p/server_nat.go.md|p2p/server_nat.go]]
- [[p2p/server_nat_test.go.md|p2p/server_nat_test.go]]
- [[p2p/util.go.md|p2p/util.go]]
- [[p2p/util_test.go.md|p2p/util_test.go]]
- [[tests/fuzzers/txfetcher/txfetcher_fuzzer.go.md|tests/fuzzers/txfetcher/txfetcher_fuzzer.go]]

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

// Package mclock is a wrapper for a monotonic clock source
package mclock

import (
...
```