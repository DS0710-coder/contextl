# keccak.go

## Architecture Metrics
- **Path:** `crypto/keccak.go`
- **Extension:** `.go`
- **Size:** 1767 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 16
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NewKeccakState`
- `Keccak256`
- `Keccak256Hash`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]

## Imported By (Dependents)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[common/types.go.md|common/types.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[core/rawdb/accessors_chain_test.go.md|core/rawdb/accessors_chain_test.go]]
- [[core/rlp_test.go.md|core/rlp_test.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[internal/blocktest/test_hash.go.md|internal/blocktest/test_hash.go]]
- [[p2p/dnsdisc/tree.go.md|p2p/dnsdisc/tree.go]]
- [[p2p/enode/idscheme.go.md|p2p/enode/idscheme.go]]
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

//go:build !ziren

package crypto

...
```