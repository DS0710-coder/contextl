# main_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h`
- **Extension:** `.h`
- **Size:** 9961 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_xonly_pubkey_load`
- `secp256k1_xonly_pubkey_save`
- `secp256k1_xonly_pubkey_parse`
- `secp256k1_xonly_pubkey_serialize`
- `secp256k1_xonly_pubkey_cmp`
- `secp256k1_extrakeys_ge_even_y`
- `secp256k1_xonly_pubkey_from_pubkey`
- `secp256k1_xonly_pubkey_tweak_add`
- `secp256k1_xonly_pubkey_tweak_add_check`
- `secp256k1_keypair_save`
- `secp256k1_keypair_seckey_load`
- `secp256k1_keypair_load`
- `secp256k1_keypair_create`
- `secp256k1_keypair_sec`
- `secp256k1_keypair_pub`
- `secp256k1_keypair_xonly_pub`
- `secp256k1_keypair_xonly_tweak_add`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Jonas Nick                                       *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_EXTRAKEYS_MAIN_H
#define SECP256K1_MODULE_EXTRAKEYS_MAIN_H

#include "../../../include/secp256k1.h"
#include "../../../include/secp256k1_extrakeys.h"
#include "../../util.h"

static SECP256K1_INLINE int secp256k1_xonly_pubkey_load(const secp256k1_context* ctx, secp256k1_ge *ge, const secp256k1_xonly_pubkey *pubkey) {
    return secp256k1_pubkey_load(ctx, ge, (const secp256k1_pubkey *) pubkey);
}

static SECP256K1_INLINE void secp256k1_xonly_pubkey_save(secp256k1_xonly_pubkey *pubkey, secp256k1_ge *ge) {
    secp256k1_pubkey_save((secp256k1_pubkey *) pubkey, ge);
}
...
```