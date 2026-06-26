# self_others.go

## Architecture Metrics
- **Path:** `internal/reexec/self_others.go`
- **Extension:** `.go`
- **Size:** 774 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Self`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// This file originates from Docker/Moby,
// https://github.com/moby/moby/blob/master/pkg/reexec/
// Licensed under Apache License 2.0: https://github.com/moby/moby/blob/master/LICENSE
// Copyright 2013-2018 Docker, Inc.

//go:build !linux

package reexec

import (
	"os"
	"os/exec"
	"path/filepath"
)

// Self returns the path to the current process's binary.
// Uses os.Args[0].
func Self() string {
	name := os.Args[0]
	if filepath.Base(name) == name {
...
```