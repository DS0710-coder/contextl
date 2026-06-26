# testrand.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/testrand.h`
- **Extension:** `.h`
- **Size:** 1886 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/testrand_impl.h.md|crypto/secp256k1/libsecp256k1/src/testrand_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/testutil.h.md|crypto/secp256k1/libsecp256k1/src/testutil.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_TESTRAND_H
#define SECP256K1_TESTRAND_H

#include "util.h"

/* A non-cryptographic RNG used only for test infrastructure. */

/** Seed the pseudorandom number generator for testing. */
SECP256K1_INLINE static void testrand_seed(const unsigned char *seed16);

/** Generate a pseudorandom number in the range [0..2**32-1]. */
SECP256K1_INLINE static uint32_t testrand32(void);

/** Generate a pseudorandom number in the range [0..2**64-1]. */
...
```