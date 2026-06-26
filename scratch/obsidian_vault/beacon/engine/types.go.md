# types.go

## Architecture Metrics
- **Path:** `beacon/engine/types.go`
- **Extension:** `.go`
- **Size:** 17117 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PayloadAttributes`
- `payloadAttributesMarshaling`
- `ExecutableData`
- `executableDataMarshaling`
- `StatelessPayloadStatusV1`
- `ExecutionPayloadEnvelope`
- `executionPayloadEnvelopeMarshaling`
- `BlobsBundle`
- `BlobAndProofV1`
- `BlobAndProofV2`
- `PayloadStatusV1`
- `TransitionConfigurationV1`
- `ForkChoiceResponse`
- `ForkchoiceStateV1`
- `ExecutionPayloadBody`
- `ClientVersionV1`
- `Version`
- `Is`
- `String`
- `MarshalText`
- `UnmarshalText`
- `encodeTransactions`
- `DecodeTransactions`
- `ExecutableDataToBlock`
- `ExecutableDataToBlockNoHash`
- `BlockToExecutableData`
- `String`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package engine

import (
	"fmt"
...
```