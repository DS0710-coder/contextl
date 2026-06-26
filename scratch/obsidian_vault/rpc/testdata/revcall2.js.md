# revcall2.js

## Architecture Metrics
- **Path:** `rpc/testdata/revcall2.js`
- **Extension:** `.js`
- **Size:** 269 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```js
// This test checks reverse calls.

--> {"jsonrpc":"2.0","id":2,"method":"test_callMeBackLater","params":["foo",[1]]}
<-- {"jsonrpc":"2.0","id":2,"result":null}
<-- {"jsonrpc":"2.0","id":1,"method":"foo","params":[1]}
--> {"jsonrpc":"2.0","id":1,"result":"my result"}

```