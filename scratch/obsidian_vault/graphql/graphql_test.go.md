# graphql_test.go

## Architecture Metrics
- **Path:** `graphql/graphql_test.go`
- **Extension:** `.go`
- **Size:** 20099 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestBuildSchema`
- `TestGraphQLBlockSerialization`
- `TestGraphQLHTTPBodyLimit`
- `TestGraphQLBlockSerializationEIP2718`
- `TestGraphQLHTTPOnSamePort_GQLRequest_Unsuccessful`
- `TestGraphQLConcurrentResolvers`
- `TestWithdrawals`
- `TestGraphQLMaxDepth`
- `createNode`
- `newGQLService`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[node/node.go.md|node/node.go]]
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

package graphql

import (
	"context"
...
```