# config.go

## Architecture Metrics
- **Path:** `cmd/geth/config.go`
- **Extension:** `.go`
- **Size:** 16423 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 21

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ethstatsConfig`
- `gethConfig`
- `loadConfig`
- `defaultNodeConfig`
- `loadBaseConfig`
- `makeConfigNode`
- `constructDevModeBanner`
- `makeFullNode`
- `dumpConfig`
- `applyMetricConfig`
- `setAccountManagerBackends`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[accounts/scwallet/apdu.go.md|accounts/scwallet/apdu.go]]
- [[accounts/usbwallet/hub.go.md|accounts/usbwallet/hub.go]]
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[common/big.go.md|common/big.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[internal/telemetry/tracesetup/setup.go.md|internal/telemetry/tracesetup/setup.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[node/node.go.md|node/node.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

package main

import (
	"bufio"
...
```