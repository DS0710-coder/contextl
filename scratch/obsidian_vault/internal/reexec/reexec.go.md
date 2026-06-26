# reexec.go

## Architecture Metrics
- **Path:** `internal/reexec/reexec.go`
- **Extension:** `.go`
- **Size:** 1167 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Register`
- `Init`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[cmd/ethkey/run_test.go.md|cmd/ethkey/run_test.go]]
- [[cmd/evm/t8n_test.go.md|cmd/evm/t8n_test.go]]
- [[cmd/geth/logging_test.go.md|cmd/geth/logging_test.go]]
- [[cmd/geth/run_test.go.md|cmd/geth/run_test.go]]
- [[internal/cmdtest/test_cmd.go.md|internal/cmdtest/test_cmd.go]]

## Source Code Snippet
```go
// This file originates from Docker/Moby,
// https://github.com/moby/moby/blob/master/pkg/reexec/reexec_deprecated.go
// Licensed under Apache License 2.0: https://github.com/moby/moby/blob/master/LICENSE
// Copyright 2013-2018 Docker, Inc.
//
// Package reexec facilitates the busybox style reexec of the docker binary that
// we require because of the forking limitations of using Go.  Handlers can be
// registered with a name and the argv 0 of the exec of the binary will be used
// to find and execute custom init paths.

package reexec

import (
	"fmt"
	"os"
)

var registeredInitializers = make(map[string]func())

// Register adds an initialization func under the specified name
...
```