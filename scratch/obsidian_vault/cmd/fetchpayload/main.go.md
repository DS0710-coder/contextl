# main.go

## Architecture Metrics
- **Path:** `cmd/fetchpayload/main.go`
- **Extension:** `.go`
- **Size:** 5421 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Payload`
- `jsonPayload`
- `main`
- `parseBlockNumber`
- `marshalJSONPayload`
- `fatal`

## Imports (Dependencies)
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/types.go.md|core/types.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

// fetchpayload queries an Ethereum node over RPC, fetches a block and its
// execution witness, and writes the combined Payload (ChainID + Block +
// Witness) to disk in the format consumed by cmd/keeper.
package main
...
```