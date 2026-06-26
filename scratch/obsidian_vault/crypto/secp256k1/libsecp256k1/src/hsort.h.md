# hsort.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/hsort.h`
- **Extension:** `.h`
- **Size:** 1685 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/hsort_impl.h.md|crypto/secp256k1/libsecp256k1/src/hsort_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2021 Russell O'Connor, Jonas Nick                     *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_HSORT_H
#define SECP256K1_HSORT_H

#include <stddef.h>
#include <string.h>

/* In-place, iterative heapsort with an interface matching glibc's qsort_r. This
 * is preferred over standard library implementations because they generally
 * make no guarantee about being fast for malicious inputs.
 * Remember that heapsort is unstable.
 *
 * In/Out: ptr: pointer to the array to sort. The contents of the array are
 *              sorted in ascending order according to the comparison function.
 * In:   count: number of elements in the array.
...
```