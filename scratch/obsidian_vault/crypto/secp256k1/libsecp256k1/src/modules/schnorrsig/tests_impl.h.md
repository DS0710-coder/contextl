# tests_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_impl.h`
- **Extension:** `.h`
- **Size:** 46225 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `nonce_function_bip340_bitflip`
- `run_nonce_function_bip340_tests`
- `test_schnorrsig_api`
- `test_schnorrsig_sha256_tagged`
- `test_schnorrsig_bip_vectors_check_signing`
- `test_schnorrsig_bip_vectors_check_verify`
- `test_schnorrsig_bip_vectors`
- `nonce_function_failing`
- `nonce_function_0`
- `nonce_function_overflowing`
- `test_schnorrsig_sign`
- `test_schnorrsig_sign_verify`
- `test_schnorrsig_taproot`
- `run_schnorrsig_tests`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2018-2020 Andrew Poelstra, Jonas Nick                 *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_SCHNORRSIG_TESTS_H
#define SECP256K1_MODULE_SCHNORRSIG_TESTS_H

#include "../../../include/secp256k1_schnorrsig.h"

/* Checks that a bit flip in the n_flip-th argument (that has n_bytes many
 * bytes) changes the hash function
 */
static void nonce_function_bip340_bitflip(unsigned char **args, size_t n_flip, size_t n_bytes, size_t msglen, size_t algolen) {
    unsigned char nonces[2][32];
    CHECK(nonce_function_bip340(nonces[0], args[0], msglen, args[1], args[2], args[3], algolen, args[4]) == 1);
    testrand_flip(args[n_flip], n_bytes);
    CHECK(nonce_function_bip340(nonces[1], args[0], msglen, args[1], args[2], args[3], algolen, args[4]) == 1);
    CHECK(secp256k1_memcmp_var(nonces[0], nonces[1], 32) != 0);
...
```