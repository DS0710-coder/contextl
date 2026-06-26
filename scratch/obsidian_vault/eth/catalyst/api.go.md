# api.go

## Architecture Metrics
- **Path:** `eth/catalyst/api.go`
- **Extension:** `.go`
- **Size:** 54682 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 18

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConsensusAPI`
- `Register`
- `NewConsensusAPI`
- `newConsensusAPIWithoutHeartbeat`
- `ForkchoiceUpdatedV1`
- `ForkchoiceUpdatedV2`
- `ForkchoiceUpdatedV3`
- `ForkchoiceUpdatedV4`
- `forkchoiceUpdated`
- `ExchangeTransitionConfigurationV1`
- `GetPayloadV1`
- `GetPayloadV2`
- `GetPayloadV3`
- `GetPayloadV4`
- `GetPayloadV5`
- `GetPayloadV6`
- `getPayload`
- `GetBlobsV1`
- `GetBlobsV2`
- `GetBlobsV3`
- `getBlobs`
- `HasBlobs`
- `NewPayloadV1`
- `NewPayloadV2`
- `NewPayloadV3`
- `NewPayloadV4`
- `NewPayloadV5`
- `newPayload`
- `delayPayloadImport`
- `setInvalidAncestor`
- `checkInvalidAncestor`
- `invalid`
- `heartbeat`
- `config`
- `checkFork`
- `ExchangeCapabilities`
- `GetClientVersionV1`
- `GetPayloadBodiesByHashV1`
- `GetPayloadBodiesByHashV2`
- `GetPayloadBodiesByRangeV1`
- `GetPayloadBodiesByRangeV2`
- `getBodiesByRange`
- `getBody`
- `convertRequests`
- `validateRequests`
- `paramsErr`
- `attributesErr`
- `unsupportedForkErr`

## Imports (Dependencies)
- [[beacon/engine/bapl_encode.go.md|beacon/engine/bapl_encode.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[internal/telemetry/telemetry.go.md|internal/telemetry/telemetry.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/format.go.md|log/format.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[params/forks/forks.go.md|params/forks/forks.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]

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

// Package catalyst implements the temporary eth1/eth2 RPC integration.
package catalyst

import (
...
```