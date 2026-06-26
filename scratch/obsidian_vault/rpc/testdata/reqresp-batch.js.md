# reqresp-batch.js

## Architecture Metrics
- **Path:** `rpc/testdata/reqresp-batch.js`
- **Extension:** `.js`
- **Size:** 464 bytes
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
// There is no response for all-notification batches.

--> [{"jsonrpc":"2.0","method":"test_echo","params":["x",99]}]

// This test checks regular batch calls.

--> [{"jsonrpc":"2.0","id":2,"method":"test_echo","params":[]}, {"jsonrpc":"2.0","id": 3,"method":"test_echo","params":["x",3]}]
<-- [{"jsonrpc":"2.0","id":2,"error":{"code":-32602,"message":"missing value for required argument 0"}},{"jsonrpc":"2.0","id":3,"result":{"String":"x","Int":3,"Args":null}}]
```