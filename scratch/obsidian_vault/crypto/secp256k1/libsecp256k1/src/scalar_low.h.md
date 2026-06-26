# scalar_low.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scalar_low.h`
- **Extension:** `.h`
- **Size:** 1135 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015, 2022 Andrew Poelstra, Pieter Wuille             *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCALAR_REPR_H
#define SECP256K1_SCALAR_REPR_H

#include <stdint.h>

/** A scalar modulo the group order of the secp256k1 curve. */
typedef uint32_t secp256k1_scalar;

/* A compile-time constant equal to 2^32 (modulo order). */
#define SCALAR_2P32 ((0xffffffffUL % EXHAUSTIVE_TEST_ORDER) + 1U)

/* Compute a*2^32 + b (modulo order). */
#define SCALAR_HORNER(a, b) (((uint64_t)(a) * SCALAR_2P32 + (b)) % EXHAUSTIVE_TEST_ORDER)

...
```