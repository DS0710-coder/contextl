# main_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h`
- **Extension:** `.h`
- **Size:** 6135 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ecdsa_recoverable_signature_load`
- `secp256k1_ecdsa_recoverable_signature_save`
- `secp256k1_ecdsa_recoverable_signature_parse_compact`
- `secp256k1_ecdsa_recoverable_signature_serialize_compact`
- `secp256k1_ecdsa_recoverable_signature_convert`
- `secp256k1_ecdsa_sig_recover`
- `secp256k1_ecdsa_sign_recoverable`
- `secp256k1_ecdsa_recover`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013-2015 Pieter Wuille                               *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_RECOVERY_MAIN_H
#define SECP256K1_MODULE_RECOVERY_MAIN_H

#include "../../../include/secp256k1_recovery.h"

static void secp256k1_ecdsa_recoverable_signature_load(const secp256k1_context* ctx, secp256k1_scalar* r, secp256k1_scalar* s, int* recid, const secp256k1_ecdsa_recoverable_signature* sig) {
    (void)ctx;
    if (sizeof(secp256k1_scalar) == 32) {
        /* When the secp256k1_scalar type is exactly 32 byte, use its
         * representation inside secp256k1_ecdsa_signature, as conversion is very fast.
         * Note that secp256k1_ecdsa_signature_save must use the same representation. */
        memcpy(r, &sig->data[0], 32);
        memcpy(s, &sig->data[32], 32);
    } else {
...
```