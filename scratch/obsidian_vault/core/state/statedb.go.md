# statedb.go

## Architecture Metrics
- **Path:** `core/state/statedb.go`
- **Extension:** `.go`
- **Size:** 53868 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `mutation`
- `StateDB`
- `removedAccountWithBalance`
- `copy`
- `isDelete`
- `New`
- `NewWithReader`
- `StartPrefetcher`
- `StopPrefetcher`
- `setError`
- `Error`
- `AddLog`
- `GetLogs`
- `Logs`
- `AddPreimage`
- `Preimages`
- `AddRefund`
- `SubRefund`
- `Exist`
- `Empty`
- `Touch`
- `GetBalance`
- `GetNonce`
- `GetStorageRoot`
- `TxIndex`
- `GetCode`
- `GetCodeSize`
- `GetCodeHash`
- `GetState`
- `GetCommittedState`
- `GetStateAndCommittedState`
- `Database`
- `Reader`
- `HasSelfDestructed`
- `AddBalance`
- `SubBalance`
- `SetBalance`
- `SetNonce`
- `SetCode`
- `SetState`
- `SetStorage`
- `SelfDestruct`
- `SetTransientState`
- `setTransientState`
- `GetTransientState`
- `updateStateObject`
- `deleteStateObject`
- `getStateObject`
- `setStateObject`
- `getOrNewStateObject`
- `createObject`
- `CreateAccount`
- `CreateContract`
- `IsNewContract`
- `Copy`
- `Snapshot`
- `RevertToSnapshot`
- `GetRefund`
- `LogsForBurnAccounts`
- `Finalise`
- `IntermediateRoot`
- `SetTxContext`
- `clearJournalAndRefund`
- `deleteStorage`
- `handleDestruction`
- `GetTrie`
- `commit`
- `commitAndFlush`
- `Commit`
- `CommitWithUpdate`
- `Prepare`
- `AddAddressToAccessList`
- `AddSlotToAccessList`
- `AddressInAccessList`
- `SlotInAccessList`
- `markDelete`
- `markUpdate`
- `Witness`
- `AccessEvents`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]

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

// Package state provides a caching layer atop the Ethereum state trie.
package state

import (
...
```