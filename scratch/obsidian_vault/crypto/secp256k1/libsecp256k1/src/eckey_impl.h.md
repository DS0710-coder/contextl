# eckey_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/eckey_impl.h`
- **Extension:** `.h`
- **Size:** 3300 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_eckey_pubkey_parse`
- `secp256k1_eckey_pubkey_serialize`
- `secp256k1_eckey_privkey_tweak_add`
- `secp256k1_eckey_pubkey_tweak_add`
- `secp256k1_eckey_privkey_tweak_mul`
- `secp256k1_eckey_pubkey_tweak_mul`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECKEY_IMPL_H
#define SECP256K1_ECKEY_IMPL_H

#include "eckey.h"

#include "scalar.h"
#include "field.h"
#include "group.h"
#include "ecmult_gen.h"

static int secp256k1_eckey_pubkey_parse(secp256k1_ge *elem, const unsigned char *pub, size_t size) {
    if (size == 33 && (pub[0] == SECP256K1_TAG_PUBKEY_EVEN || pub[0] == SECP256K1_TAG_PUBKEY_ODD)) {
        secp256k1_fe x;
        return secp256k1_fe_set_b32_limit(&x, pub+1) && secp256k1_ge_set_xo_var(elem, &x, pub[0] == SECP256K1_TAG_PUBKEY_ODD);
...
```