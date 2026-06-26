# internal-error.js

## Architecture Metrics
- **Path:** `rpc/testdata/internal-error.js`
- **Extension:** `.js`
- **Size:** 425 bytes
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
// These tests trigger various 'internal error' conditions.

--> {"jsonrpc":"2.0","id":1,"method":"test_marshalError","params": []}
<-- {"jsonrpc":"2.0","id":1,"error":{"code":-32603,"message":"json: error calling MarshalText for type *rpc.MarshalErrObj: marshal error"}}

--> {"jsonrpc":"2.0","id":2,"method":"test_panic","params": []}
<-- {"jsonrpc":"2.0","id":2,"error":{"code":-32603,"message":"method handler crashed"}}
```