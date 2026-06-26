# invalid-idonly.js

## Architecture Metrics
- **Path:** `rpc/testdata/invalid-idonly.js`
- **Extension:** `.js`
- **Size:** 292 bytes
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
// This test checks processing of messages that contain just the ID and nothing else.

--> {"id":1}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}

--> {"jsonrpc":"2.0","id":1}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32600,"message":"invalid request"}}
```