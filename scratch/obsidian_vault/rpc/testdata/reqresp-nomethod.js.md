# reqresp-nomethod.js

## Architecture Metrics
- **Path:** `rpc/testdata/reqresp-nomethod.js`
- **Extension:** `.js`
- **Size:** 250 bytes
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
// This test calls a method that doesn't exist.

--> {"jsonrpc": "2.0", "id": 2, "method": "invalid_method", "params": [2, 3]}
<-- {"jsonrpc":"2.0","id":2,"error":{"code":-32601,"message":"the method invalid_method does not exist/is not available"}}
```