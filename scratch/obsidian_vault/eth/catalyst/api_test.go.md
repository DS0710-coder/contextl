# api_test.go

## Architecture Metrics
- **Path:** `eth/catalyst/api_test.go`
- **Extension:** `.go`
- **Size:** 69173 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 20

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test`
- `generateMergeChain`
- `TestEth2AssembleBlock`
- `assembleWithTransactions`
- `TestEth2AssembleBlockWithAnotherBlocksTxs`
- `TestEth2PrepareAndGetPayload`
- `checkLogEvents`
- `TestInvalidPayloadTimestamp`
- `TestEth2NewBlock`
- `TestEth2DeepReorg`
- `startEthService`
- `TestFullAPI`
- `setupBlocks`
- `TestExchangeTransitionConfig`
- `TestNewPayloadOnInvalidChain`
- `assembleEnvelope`
- `assembleBlock`
- `TestEmptyBlocks`
- `getNewEnvelope`
- `getNewPayload`
- `setBlockhash`
- `decodeTransactions`
- `TestTrickRemoteBlockCache`
- `TestInvalidBloom`
- `TestSimultaneousNewBlock`
- `TestWithdrawals`
- `TestNilWithdrawals`
- `setupBodies`
- `allHashes`
- `allBodies`
- `TestGetBlockBodiesByHash`
- `TestGetBlockBodiesByRange`
- `TestGetBlockBodiesByRangeInvalidParams`
- `checkEqualBody`
- `TestBlockToPayloadWithBlobs`
- `TestParentBeaconBlockRoot`
- `TestWitnessCreationAndConsumption`
- `TestGetClientVersion`
- `TestValidateRequests`
- `init`
- `makeMultiBlobTx`
- `newGetBlobEnv`
- `TestGetBlobsV2And3`
- `BenchmarkGetBlobsV2`
- `runGetBlobs`

## Imports (Dependencies)
- [[beacon/engine/bapl_encode.go.md|beacon/engine/bapl_encode.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[internal/testrand/rand.go.md|internal/testrand/rand.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[node/node.go.md|node/node.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package catalyst

import (
	"bytes"
...
```