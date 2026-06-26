# abi.go

## Architecture Metrics
- **Path:** `accounts/abi/abi.go`
- **Extension:** `.go`
- **Size:** 10805 bytes
- **Centrality Score:** 0.0018
- **In-Degree (Imported By):** 24
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ABI`
- `JSON`
- `Pack`
- `getArguments`
- `Unpack`
- `UnpackIntoInterface`
- `UnpackIntoMap`
- `UnmarshalJSON`
- `MethodById`
- `EventByID`
- `ErrorByID`
- `HasFallback`
- `HasReceive`
- `UnpackRevert`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
- [[accounts/abi/abigen/bind.go.md|accounts/abi/abigen/bind.go]]
- [[accounts/abi/abigen/bindv2.go.md|accounts/abi/abigen/bindv2.go]]
- [[accounts/abi/abigen/bindv2_test.go.md|accounts/abi/abigen/bindv2_test.go]]
- [[accounts/abi/abigen/template.go.md|accounts/abi/abigen/template.go]]
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/base.go.md|accounts/abi/bind/v2/base.go]]
- [[accounts/abi/bind/v2/base_test.go.md|accounts/abi/bind/v2/base_test.go]]
- [[accounts/abi/bind/v2/internal/contracts/db/bindings.go.md|accounts/abi/bind/v2/internal/contracts/db/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/events/bindings.go.md|accounts/abi/bind/v2/internal/contracts/events/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/nested_libraries/bindings.go.md|accounts/abi/bind/v2/internal/contracts/nested_libraries/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/solc_errors/bindings.go.md|accounts/abi/bind/v2/internal/contracts/solc_errors/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/uint256arrayreturn/bindings.go.md|accounts/abi/bind/v2/internal/contracts/uint256arrayreturn/bindings.go]]
- [[accounts/abi/bind/v2/lib.go.md|accounts/abi/bind/v2/lib.go]]
- [[core/types/deposit_test.go.md|core/types/deposit_test.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/tracers/native/call.go.md|eth/tracers/native/call.go]]
- [[eth/tracers/native/erc7562.go.md|eth/tracers/native/erc7562.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/errors.go.md|internal/ethapi/errors.go]]
- [[signer/fourbyte/abi.go.md|signer/fourbyte/abi.go]]
- [[signer/fourbyte/abi_test.go.md|signer/fourbyte/abi_test.go]]
- [[signer/fourbyte/fourbyte_test.go.md|signer/fourbyte/fourbyte_test.go]]

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package abi

import (
	"bytes"
...
```