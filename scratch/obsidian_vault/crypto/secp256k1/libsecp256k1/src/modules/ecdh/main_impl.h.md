# main_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h`
- **Extension:** `.h`
- **Size:** 2482 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ecdh_hash_function_sha256`
- `secp256k1_ecdh`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ECDH_MAIN_H
#define SECP256K1_MODULE_ECDH_MAIN_H

#include "../../../include/secp256k1_ecdh.h"
#include "../../ecmult_const_impl.h"

static int ecdh_hash_function_sha256(unsigned char *output, const unsigned char *x32, const unsigned char *y32, void *data) {
    unsigned char version = (y32[31] & 0x01) | 0x02;
    secp256k1_sha256 sha;
    (void)data;

    secp256k1_sha256_initialize(&sha);
    secp256k1_sha256_write(&sha, &version, 1);
    secp256k1_sha256_write(&sha, x32, 32);
...
```