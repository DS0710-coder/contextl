# tests_exhaustive_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h`
- **Extension:** `.h`
- **Size:** 1700 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test_exhaustive_ellswift`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ELLSWIFT_TESTS_EXHAUSTIVE_H
#define SECP256K1_MODULE_ELLSWIFT_TESTS_EXHAUSTIVE_H

#include "../../../include/secp256k1_ellswift.h"
#include "main_impl.h"

static void test_exhaustive_ellswift(const secp256k1_context *ctx, const secp256k1_ge *group) {
    int i;

    /* Note that SwiftEC/ElligatorSwift are inherently curve operations, not
     * group operations, and this test only checks the curve points which are in
     * a tiny subgroup. In that sense it can't be really seen as exhaustive as
     * it doesn't (and for computational reasons obviously cannot) test the
     * entire domain ellswift operates under. */
    for (i = 1; i < EXHAUSTIVE_TEST_ORDER; i++) {
...
```