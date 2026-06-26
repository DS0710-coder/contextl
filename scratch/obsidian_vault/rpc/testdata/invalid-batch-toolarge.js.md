# invalid-batch-toolarge.js

## Architecture Metrics
- **Path:** `rpc/testdata/invalid-batch-toolarge.js`
- **Extension:** `.js`
- **Size:** 1104 bytes
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
// This file checks the behavior of the batch item limit code.
// In tests, the batch item limit is set to 4. So to trigger the error,
// all batches in this file have 5 elements.

// For batches that do not contain any calls, a response message with "id" == null
// is returned.

--> [{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]}]
<-- [{"jsonrpc":"2.0","id":null,"error":{"code":-32600,"message":"batch too large"}}]

// For batches with at least one call, the call's "id" is used.
--> [{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","id":3,"method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]},{"jsonrpc":"2.0","method":"test_echo","params":["x",99]}]
<-- [{"jsonrpc":"2.0","id":3,"error":{"code":-32600,"message":"batch too large"}}]
```