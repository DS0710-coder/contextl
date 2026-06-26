# main_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h`
- **Extension:** `.h`
- **Size:** 10192 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_nonce_function_bip340_sha256_tagged`
- `secp256k1_nonce_function_bip340_sha256_tagged_aux`
- `nonce_function_bip340`
- `secp256k1_schnorrsig_sha256_tagged`
- `secp256k1_schnorrsig_challenge`
- `secp256k1_schnorrsig_sign_internal`
- `secp256k1_schnorrsig_sign32`
- `secp256k1_schnorrsig_sign`
- `secp256k1_schnorrsig_sign_custom`
- `secp256k1_schnorrsig_verify`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2018-2020 Andrew Poelstra, Jonas Nick                 *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_SCHNORRSIG_MAIN_H
#define SECP256K1_MODULE_SCHNORRSIG_MAIN_H

#include "../../../include/secp256k1.h"
#include "../../../include/secp256k1_schnorrsig.h"
#include "../../hash.h"

/* Initializes SHA256 with fixed midstate. This midstate was computed by applying
 * SHA256 to SHA256("BIP0340/nonce")||SHA256("BIP0340/nonce"). */
static void secp256k1_nonce_function_bip340_sha256_tagged(secp256k1_sha256 *sha) {
    secp256k1_sha256_initialize(sha);
    sha->s[0] = 0x46615b35ul;
    sha->s[1] = 0xf4bfbff7ul;
    sha->s[2] = 0x9f8dc671ul;
...
```