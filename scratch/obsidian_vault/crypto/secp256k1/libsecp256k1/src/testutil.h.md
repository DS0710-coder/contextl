# testutil.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/testutil.h`
- **Extension:** `.h`
- **Size:** 4163 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testutil_random_fe`
- `testutil_random_fe_non_zero`
- `testutil_random_fe_magnitude`
- `testutil_random_fe_test`
- `testutil_random_fe_non_zero_test`
- `testutil_random_ge_x_magnitude`
- `testutil_random_ge_y_magnitude`
- `testutil_random_gej_x_magnitude`
- `testutil_random_gej_y_magnitude`
- `testutil_random_gej_z_magnitude`
- `testutil_random_ge_test`
- `testutil_random_ge_jacobian_test`
- `testutil_random_gej_test`
- `testutil_random_pubkey_test`
- `testutil_random_scalar_order_test`
- `testutil_random_scalar_order`
- `testutil_random_scalar_order_b32`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/testrand.h.md|crypto/secp256k1/libsecp256k1/src/testrand.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_TESTUTIL_H
#define SECP256K1_TESTUTIL_H

#include "field.h"
#include "group.h"
#include "testrand.h"
#include "util.h"

static void testutil_random_fe(secp256k1_fe *x) {
    unsigned char bin[32];
    do {
        testrand256(bin);
        if (secp256k1_fe_set_b32_limit(x, bin)) {
            return;
        }
...
```