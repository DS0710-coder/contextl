# tx_blob.go

## Architecture Metrics
- **Path:** `core/types/tx_blob.go`
- **Extension:** `.go`
- **Size:** 12989 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlobTx`
- `BlobTxSidecar`
- `blobTxWithBlobs`
- `blobTxWithBlobsV0`
- `blobTxWithBlobsV1`
- `NewBlobTxSidecar`
- `BlobHashes`
- `CellProofsAt`
- `ToV1`
- `encodedSize`
- `ValidateBlobCommitmentHashes`
- `Copy`
- `tx`
- `assign`
- `tx`
- `assign`
- `copy`
- `txType`
- `chainID`
- `accessList`
- `data`
- `gas`
- `gasFeeCap`
- `gasTipCap`
- `gasPrice`
- `value`
- `nonce`
- `to`
- `blobGas`
- `effectiveGasPrice`
- `rawSignatureValues`
- `setSignatureValues`
- `withoutSidecar`
- `withSidecar`
- `encode`
- `decode`
- `sigHash`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package types

import (
	"bytes"
...
```