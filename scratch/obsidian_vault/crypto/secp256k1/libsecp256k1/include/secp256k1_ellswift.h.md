# secp256k1_ellswift.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h`
- **Extension:** `.h`
- **Size:** 9117 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/ellswift.c.md|crypto/secp256k1/libsecp256k1/examples/ellswift.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_ELLSWIFT_H
#define SECP256K1_ELLSWIFT_H

#include "secp256k1.h"

#ifdef __cplusplus
extern "C" {
#endif

/* This module provides an implementation of ElligatorSwift as well as a
 * version of x-only ECDH using it (including compatibility with BIP324).
 *
 * ElligatorSwift is described in https://eprint.iacr.org/2022/759 by
 * Chavez-Saab, Rodriguez-Henriquez, and Tibouchi. It permits encoding
 * uniformly chosen public keys as 64-byte arrays which are indistinguishable
 * from uniformly random arrays.
 *
 * Let f be the function from pairs of field elements to point X coordinates,
 * defined as follows (all operations modulo p = 2^256 - 2^32 - 977)
 * f(u,t):
...
```