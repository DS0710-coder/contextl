# secp256k1_ecdh.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h`
- **Extension:** `.h`
- **Size:** 2560 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/ecdh.c.md|crypto/secp256k1/libsecp256k1/examples/ecdh.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_ECDH_H
#define SECP256K1_ECDH_H

#include "secp256k1.h"

#ifdef __cplusplus
extern "C" {
#endif

/** A pointer to a function that hashes an EC point to obtain an ECDH secret
 *
 *  Returns: 1 if the point was successfully hashed.
 *           0 will cause secp256k1_ecdh to fail and return 0.
 *           Other return values are not allowed, and the behaviour of
 *           secp256k1_ecdh is undefined for other return values.
 *  Out:     output:     pointer to an array to be filled by the function
 *  In:      x32:        pointer to a 32-byte x coordinate
 *           y32:        pointer to a 32-byte y coordinate
 *           data:       arbitrary data pointer that is passed through
 */
...
```