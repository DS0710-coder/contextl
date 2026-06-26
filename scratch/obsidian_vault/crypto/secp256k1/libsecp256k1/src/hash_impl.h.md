# hash_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/hash_impl.h`
- **Extension:** `.h`
- **Size:** 13572 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_sha256_initialize`
- `secp256k1_sha256_transform`
- `secp256k1_sha256_write`
- `secp256k1_sha256_finalize`
- `secp256k1_sha256_initialize_tagged`
- `secp256k1_sha256_clear`
- `secp256k1_hmac_sha256_initialize`
- `secp256k1_hmac_sha256_write`
- `secp256k1_hmac_sha256_finalize`
- `secp256k1_hmac_sha256_clear`
- `secp256k1_rfc6979_hmac_sha256_initialize`
- `secp256k1_rfc6979_hmac_sha256_generate`
- `secp256k1_rfc6979_hmac_sha256_finalize`
- `secp256k1_rfc6979_hmac_sha256_clear`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_HASH_IMPL_H
#define SECP256K1_HASH_IMPL_H

#include "hash.h"
#include "util.h"

#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define Ch(x,y,z) ((z) ^ ((x) & ((y) ^ (z))))
#define Maj(x,y,z) (((x) & (y)) | ((z) & ((x) | (y))))
#define Sigma0(x) (((x) >> 2 | (x) << 30) ^ ((x) >> 13 | (x) << 19) ^ ((x) >> 22 | (x) << 10))
#define Sigma1(x) (((x) >> 6 | (x) << 26) ^ ((x) >> 11 | (x) << 21) ^ ((x) >> 25 | (x) << 7))
...
```