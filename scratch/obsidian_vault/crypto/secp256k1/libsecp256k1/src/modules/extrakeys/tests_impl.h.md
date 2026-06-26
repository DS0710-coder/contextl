# tests_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_impl.h`
- **Extension:** `.h`
- **Size:** 23346 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test_xonly_pubkey`
- `test_xonly_pubkey_comparison`
- `test_xonly_pubkey_tweak`
- `test_xonly_pubkey_tweak_check`
- `test_xonly_pubkey_tweak_recursive`
- `test_keypair`
- `test_keypair_add`
- `run_extrakeys_tests`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Jonas Nick                                       *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_EXTRAKEYS_TESTS_H
#define SECP256K1_MODULE_EXTRAKEYS_TESTS_H

#include "../../../include/secp256k1_extrakeys.h"

static void test_xonly_pubkey(void) {
    secp256k1_pubkey pk;
    secp256k1_xonly_pubkey xonly_pk, xonly_pk_tmp;
    secp256k1_ge pk1;
    secp256k1_ge pk2;
    secp256k1_fe y;
    unsigned char sk[32];
    unsigned char xy_sk[32];
    unsigned char buf32[32];
...
```