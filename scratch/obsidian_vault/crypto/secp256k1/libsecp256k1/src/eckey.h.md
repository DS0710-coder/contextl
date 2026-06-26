# eckey.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/eckey.h`
- **Extension:** `.h`
- **Size:** 1163 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/eckey_impl.h.md|crypto/secp256k1/libsecp256k1/src/eckey_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECKEY_H
#define SECP256K1_ECKEY_H

#include <stddef.h>

#include "group.h"
#include "scalar.h"
#include "ecmult.h"
#include "ecmult_gen.h"

static int secp256k1_eckey_pubkey_parse(secp256k1_ge *elem, const unsigned char *pub, size_t size);
static int secp256k1_eckey_pubkey_serialize(secp256k1_ge *elem, unsigned char *pub, size_t *size, int compressed);

static int secp256k1_eckey_privkey_tweak_add(secp256k1_scalar *key, const secp256k1_scalar *tweak);
...
```