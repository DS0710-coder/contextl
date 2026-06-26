# tests_exhaustive.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c`
- **Extension:** `.c`
- **Size:** 18760 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `skip_section`
- `secp256k1_nonce_function_smallint`
- `test_exhaustive_endomorphism`
- `test_exhaustive_addition`
- `test_exhaustive_ecmult`
- `ecmult_multi_callback`
- `test_exhaustive_ecmult_multi`
- `r_from_k`
- `test_exhaustive_verify`
- `test_exhaustive_sign`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/testrand_impl.h.md|crypto/secp256k1/libsecp256k1/src/testrand_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/testutil.h.md|crypto/secp256k1/libsecp256k1/src/testutil.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2016 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef EXHAUSTIVE_TEST_ORDER
/* see group_impl.h for allowable values */
#define EXHAUSTIVE_TEST_ORDER 13
#endif

/* These values of B are all values in [1, 8] that result in a curve with even order. */
#define EXHAUSTIVE_TEST_CURVE_HAS_EVEN_ORDER (SECP256K1_B == 1 || SECP256K1_B == 6 || SECP256K1_B == 8)

#ifdef USE_EXTERNAL_DEFAULT_CALLBACKS
    #pragma message("Ignoring USE_EXTERNAL_CALLBACKS in exhaustive_tests.")
...
```