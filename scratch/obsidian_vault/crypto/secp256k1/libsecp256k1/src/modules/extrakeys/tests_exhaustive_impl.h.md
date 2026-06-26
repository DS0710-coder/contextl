# tests_exhaustive_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h`
- **Extension:** `.h`
- **Size:** 3221 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test_exhaustive_extrakeys`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_EXTRAKEYS_TESTS_EXHAUSTIVE_H
#define SECP256K1_MODULE_EXTRAKEYS_TESTS_EXHAUSTIVE_H

#include "../../../include/secp256k1_extrakeys.h"
#include "main_impl.h"

static void test_exhaustive_extrakeys(const secp256k1_context *ctx, const secp256k1_ge* group) {
    secp256k1_keypair keypair[EXHAUSTIVE_TEST_ORDER - 1];
    secp256k1_pubkey pubkey[EXHAUSTIVE_TEST_ORDER - 1];
    secp256k1_xonly_pubkey xonly_pubkey[EXHAUSTIVE_TEST_ORDER - 1];
    int parities[EXHAUSTIVE_TEST_ORDER - 1];
    unsigned char xonly_pubkey_bytes[EXHAUSTIVE_TEST_ORDER - 1][32];
    int i;

...
```