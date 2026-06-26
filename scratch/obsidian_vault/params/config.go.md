# config.go

## Architecture Metrics
- **Path:** `params/config.go`
- **Extension:** `.go`
- **Size:** 58003 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChainConfig`
- `EthashConfig`
- `CliqueConfig`
- `BlobConfig`
- `BlobScheduleConfig`
- `fork`
- `ConfigCompatError`
- `Rules`
- `newUint64`
- `String`
- `String`
- `String`
- `Description`
- `String`
- `IsHomestead`
- `IsDAOFork`
- `IsEIP150`
- `IsEIP155`
- `IsEIP158`
- `IsByzantium`
- `IsConstantinople`
- `IsMuirGlacier`
- `IsPetersburg`
- `IsIstanbul`
- `IsBerlin`
- `IsLondon`
- `IsArrowGlacier`
- `IsGrayGlacier`
- `IsTerminalPoWBlock`
- `IsPostMerge`
- `IsShanghai`
- `IsCancun`
- `IsPrague`
- `IsOsaka`
- `IsBPO1`
- `IsBPO2`
- `IsBPO3`
- `IsBPO4`
- `IsBPO5`
- `IsAmsterdam`
- `IsUBT`
- `IsUBTGenesis`
- `IsEIP4762`
- `CheckCompatible`
- `CheckConfigForkOrder`
- `validate`
- `checkCompatible`
- `BaseFeeChangeDenominator`
- `ElasticityMultiplier`
- `LatestFork`
- `BlobConfig`
- `ActiveSystemContracts`
- `Timestamp`
- `isForkBlockIncompatible`
- `isBlockForked`
- `configBlockEqual`
- `isForkTimestampIncompatible`
- `isTimestampForked`
- `configTimestampEqual`
- `newBlockCompatError`
- `newTimestampCompatError`
- `Error`
- `Rules`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[params/forks/forks.go.md|params/forks/forks.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package params

import (
	"errors"
...
```