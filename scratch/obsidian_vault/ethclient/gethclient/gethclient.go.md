# gethclient.go

## Architecture Metrics
- **Path:** `ethclient/gethclient/gethclient.go`
- **Extension:** `.go`
- **Size:** 14913 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Client`
- `accessListResult`
- `AccountResult`
- `StorageResult`
- `storageResult`
- `accountResult`
- `CallTracerConfig`
- `CallLog`
- `callLogMarshaling`
- `CallFrame`
- `callFrameMarshaling`
- `traceCallConfig`
- `New`
- `CreateAccessList`
- `GetProof`
- `CallContract`
- `CallContractWithBlockOverrides`
- `GCStats`
- `MemStats`
- `SetHead`
- `GetNodeInfo`
- `SubscribeFullPendingTransactions`
- `SubscribePendingTransactions`
- `TraceTransaction`
- `TraceBlock`
- `TraceTransactionWithCallTracer`
- `TraceCallWithCallTracer`
- `callTracerConfig`
- `callTraceCallConfig`
- `toBlockNumArg`
- `toCallArg`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/workload/client.go.md|cmd/workload/client.go]]

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

// Package gethclient provides an RPC client for geth-specific APIs.
package gethclient

import (
...
```