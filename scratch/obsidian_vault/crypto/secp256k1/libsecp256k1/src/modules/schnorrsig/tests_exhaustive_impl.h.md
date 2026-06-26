# tests_exhaustive_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h`
- **Extension:** `.h`
- **Size:** 10135 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_hardened_nonce_function_smallint`
- `test_exhaustive_schnorrsig_verify`
- `test_exhaustive_schnorrsig_sign`
- `test_exhaustive_schnorrsig`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_SCHNORRSIG_TESTS_EXHAUSTIVE_H
#define SECP256K1_MODULE_SCHNORRSIG_TESTS_EXHAUSTIVE_H

#include "../../../include/secp256k1_schnorrsig.h"
#include "main_impl.h"

static const unsigned char invalid_pubkey_bytes[][32] = {
    /* 0 */
    {
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    },
    /* 2 */
    {
...
```