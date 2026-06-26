# hsort_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/hsort_impl.h`
- **Extension:** `.h`
- **Size:** 4798 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_heap_child1`
- `secp256k1_heap_child2`
- `secp256k1_heap_swap64`
- `secp256k1_heap_swap`
- `secp256k1_heap_down`
- `secp256k1_hsort`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/hsort.h.md|crypto/secp256k1/libsecp256k1/src/hsort.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2021 Russell O'Connor, Jonas Nick                     *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_HSORT_IMPL_H
#define SECP256K1_HSORT_IMPL_H

#include "hsort.h"

/* An array is a heap when, for all non-zero indexes i, the element at index i
 * compares as less than or equal to the element at index parent(i) = (i-1)/2.
 */

static SECP256K1_INLINE size_t secp256k1_heap_child1(size_t i) {
    VERIFY_CHECK(i <= (SIZE_MAX - 1)/2);
    return 2*i + 1;
}

...
```