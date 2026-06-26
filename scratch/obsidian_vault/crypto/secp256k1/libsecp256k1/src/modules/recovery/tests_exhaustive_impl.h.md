# tests_exhaustive_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h`
- **Extension:** `.h`
- **Size:** 7733 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test_exhaustive_recovery_sign`
- `test_exhaustive_recovery_verify`
- `test_exhaustive_recovery`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2016 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_RECOVERY_EXHAUSTIVE_TESTS_H
#define SECP256K1_MODULE_RECOVERY_EXHAUSTIVE_TESTS_H

#include "main_impl.h"
#include "../../../include/secp256k1_recovery.h"

static void test_exhaustive_recovery_sign(const secp256k1_context *ctx, const secp256k1_ge *group) {
    int i, j, k;
    uint64_t iter = 0;

    /* Loop */
    for (i = 1; i < EXHAUSTIVE_TEST_ORDER; i++) {  /* message */
        for (j = 1; j < EXHAUSTIVE_TEST_ORDER; j++) {  /* key */
            if (skip_section(&iter)) continue;
...
```