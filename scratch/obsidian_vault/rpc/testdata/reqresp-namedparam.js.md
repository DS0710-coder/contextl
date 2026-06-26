# reqresp-namedparam.js

## Architecture Metrics
- **Path:** `rpc/testdata/reqresp-namedparam.js`
- **Extension:** `.js`
- **Size:** 239 bytes
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
// This test checks that an error response is sent for calls
// with named parameters. 

--> {"jsonrpc":"2.0","method":"test_echo","params":{"int":23},"id":3}
<-- {"jsonrpc":"2.0","id":3,"error":{"code":-32602,"message":"non-array args"}}
```