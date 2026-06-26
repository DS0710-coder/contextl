# tx_fetcher_test.go

## Architecture Metrics
- **Path:** `eth/fetcher/tx_fetcher_test.go`
- **Extension:** `.go`
- **Size:** 76522 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `announce`
- `doTxNotify`
- `doTxEnqueue`
- `doWait`
- `isScheduled`
- `txFetcherTest`
- `newTestTxFetcher`
- `TestTransactionFetcherWaiting`
- `TestTransactionFetcherSkipWaiting`
- `TestTransactionFetcherSingletonRequesting`
- `TestTransactionFetcherFailedRescheduling`
- `TestTransactionFetcherCleanup`
- `TestTransactionFetcherCleanupEmpty`
- `TestTransactionFetcherMissingRescheduling`
- `TestTransactionFetcherMissingCleanup`
- `TestTransactionFetcherBroadcasts`
- `TestTransactionFetcherWaitTimerResets`
- `TestTransactionFetcherTimeoutRescheduling`
- `TestTransactionFetcherTimeoutTimerResets`
- `TestTransactionFetcherRateLimiting`
- `TestTransactionFetcherBandwidthLimiting`
- `TestTransactionFetcherDoSProtection`
- `TestTransactionFetcherUnderpricedDedup`
- `TestTransactionFetcherUnderpricedDoSProtection`
- `TestTransactionFetcherOutOfBoundDeliveries`
- `TestTransactionFetcherDrop`
- `TestTransactionFetcherDropRescheduling`
- `TestInvalidAnnounceMetadata`
- `TestTransactionFetcherFuzzCrash01`
- `TestTransactionFetcherFuzzCrash02`
- `TestTransactionFetcherFuzzCrash03`
- `TestTransactionFetcherFuzzCrash04`
- `TestBlobTransactionAnnounce`
- `TestTransactionFetcherDropAlternates`
- `TestTransactionFetcherWrongMetadata`
- `makeInvalidBlobTx`
- `TestTransactionProtocolViolation`
- `testTransactionFetcherParallel`
- `testTransactionFetcher`
- `containsAnnounce`
- `containsHashInAnnounces`
- `TestTransactionForgotten`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

package fetcher

import (
	"crypto/sha256"
...
```