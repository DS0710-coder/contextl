# transaction.go

## Architecture Metrics
- **Path:** `core/types/transaction.go`
- **Extension:** `.go`
- **Size:** 20941 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Transaction`
- `TxData`
- `NewTx`
- `EncodeRLP`
- `encodeTyped`
- `MarshalBinary`
- `DecodeRLP`
- `UnmarshalBinary`
- `decodeTyped`
- `setDecoded`
- `sanityCheckSignature`
- `isProtectedV`
- `Protected`
- `Type`
- `ChainId`
- `Data`
- `AccessList`
- `Gas`
- `GasPrice`
- `GasTipCap`
- `GasFeeCap`
- `Value`
- `Nonce`
- `To`
- `Cost`
- `RawSignatureValues`
- `GasFeeCapCmp`
- `GasFeeCapIntCmp`
- `GasTipCapCmp`
- `GasTipCapIntCmp`
- `EffectiveGasTip`
- `calcEffectiveGasTip`
- `EffectiveGasTipValue`
- `EffectiveGasTipCmp`
- `EffectiveGasTipIntCmp`
- `BlobGas`
- `BlobGasFeeCap`
- `BlobHashes`
- `BlobTxSidecar`
- `BlobGasFeeCapCmp`
- `BlobGasFeeCapIntCmp`
- `WithoutBlobTxSidecar`
- `WithBlobTxSidecar`
- `SetCodeAuthorizations`
- `SetCodeAuthorities`
- `SetTime`
- `Time`
- `Hash`
- `Size`
- `WithSignature`
- `Len`
- `EncodeIndex`
- `TxDifference`
- `HashDifference`
- `Len`
- `Less`
- `Swap`
- `copyAddressPtr`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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