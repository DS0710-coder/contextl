# prompter.go

## Architecture Metrics
- **Path:** `console/prompt/prompter.go`
- **Extension:** `.go`
- **Size:** 6289 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UserPrompter`
- `terminalPrompter`
- `newTerminalPrompter`
- `PromptInput`
- `PromptPassword`
- `PromptConfirm`
- `SetHistory`
- `AppendHistory`
- `ClearHistory`
- `SetWordCompleter`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[cmd/devp2p/dnscmd.go.md|cmd/devp2p/dnscmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/utils/prompt.go.md|cmd/utils/prompt.go]]
- [[console/bridge.go.md|console/bridge.go]]
- [[console/console.go.md|console/console.go]]
- [[console/console_test.go.md|console/console_test.go]]

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

package prompt

import (
	"fmt"
...
```