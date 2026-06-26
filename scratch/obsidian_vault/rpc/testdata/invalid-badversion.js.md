# invalid-badversion.js

## Architecture Metrics
- **Path:** `rpc/testdata/invalid-badversion.js`
- **Extension:** `.js`
- **Size:** 943 bytes
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
// This test checks processing of messages with invalid Version.

--> {"jsonrpc":"2.0","id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"result":{"String":"x","Int":3,"Args":null}}

--> {"jsonrpc":"2.1","id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}

--> {"jsonrpc":"go-ethereum","id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}

--> {"jsonrpc":1,"id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}

--> {"jsonrpc":2.0,"id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}

--> {"id":1,"method":"test_echo","params":["x", 3]}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}
```