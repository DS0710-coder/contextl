# tests_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ecdh/tests_impl.h`
- **Extension:** `.h`
- **Size:** 5789 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ecdh_hash_function_test_fail`
- `ecdh_hash_function_custom`
- `test_ecdh_api`
- `test_ecdh_generator_basepoint`
- `test_bad_scalar`
- `test_result_basepoint`
- `run_ecdh_tests`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ECDH_TESTS_H
#define SECP256K1_MODULE_ECDH_TESTS_H

static int ecdh_hash_function_test_fail(unsigned char *output, const unsigned char *x, const unsigned char *y, void *data) {
    (void)output;
    (void)x;
    (void)y;
    (void)data;
    return 0;
}

static int ecdh_hash_function_custom(unsigned char *output, const unsigned char *x, const unsigned char *y, void *data) {
    (void)data;
    /* Save x and y as uncompressed public key */
...
```