# ecmult_gen_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h`
- **Extension:** `.h`
- **Size:** 16367 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ecmult_gen_context_build`
- `secp256k1_ecmult_gen_context_is_built`
- `secp256k1_ecmult_gen_context_clear`
- `secp256k1_ecmult_gen_scalar_diff`
- `secp256k1_ecmult_gen`
- `secp256k1_ecmult_gen_blind`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash_impl.h.md|crypto/secp256k1/libsecp256k1/src/hash_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) Pieter Wuille, Gregory Maxwell, Peter Dettman         *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECMULT_GEN_IMPL_H
#define SECP256K1_ECMULT_GEN_IMPL_H

#include "util.h"
#include "scalar.h"
#include "group.h"
#include "ecmult_gen.h"
#include "hash_impl.h"
#include "precomputed_ecmult_gen.h"

static void secp256k1_ecmult_gen_context_build(secp256k1_ecmult_gen_context *ctx) {
    secp256k1_ecmult_gen_blind(ctx, NULL);
    ctx->built = 1;
}
...
```