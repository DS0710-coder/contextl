# reqresp-echo.js

## Architecture Metrics
- **Path:** `rpc/testdata/reqresp-echo.js`
- **Extension:** `.js`
- **Size:** 886 bytes
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
// This test calls the test_echo method.

--> {"jsonrpc": "2.0", "id": 2, "method": "test_echo", "params": []}
<-- {"jsonrpc":"2.0","id":2,"error":{"code":-32602,"message":"missing value for required argument 0"}}

--> {"jsonrpc": "2.0", "id": 2, "method": "test_echo", "params": ["x"]}
<-- {"jsonrpc":"2.0","id":2,"error":{"code":-32602,"message":"missing value for required argument 1"}}

--> {"jsonrpc": "2.0", "id": 2, "method": "test_echo", "params": ["x", 3]}
<-- {"jsonrpc":"2.0","id":2,"result":{"String":"x","Int":3,"Args":null}}

--> {"jsonrpc": "2.0", "id": 2, "method": "test_echo", "params": ["x", 3, {"S": "foo"}]}
<-- {"jsonrpc":"2.0","id":2,"result":{"String":"x","Int":3,"Args":{"S":"foo"}}}

--> {"jsonrpc": "2.0", "id": 2, "method": "test_echoWithCtx", "params": ["x", 3, {"S": "foo"}]}
<-- {"jsonrpc":"2.0","id":2,"result":{"String":"x","Int":3,"Args":{"S":"foo"}}}
```