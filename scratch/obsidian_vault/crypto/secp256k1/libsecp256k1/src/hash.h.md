# hash.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/hash.h`
- **Extension:** `.h`
- **Size:** 1916 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 8
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/hash_impl.h.md|crypto/secp256k1/libsecp256k1/src/hash_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/selftest.h.md|crypto/secp256k1/libsecp256k1/src/selftest.h]]
- [[crypto/secp256k1/libsecp256k1/src/testrand_impl.h.md|crypto/secp256k1/libsecp256k1/src/testrand_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_HASH_H
#define SECP256K1_HASH_H

#include <stdlib.h>
#include <stdint.h>

typedef struct {
    uint32_t s[8];
    unsigned char buf[64];
    uint64_t bytes;
} secp256k1_sha256;

static void secp256k1_sha256_initialize(secp256k1_sha256 *hash);
static void secp256k1_sha256_write(secp256k1_sha256 *hash, const unsigned char *data, size_t size);
...
```