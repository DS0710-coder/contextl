# keyagg_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h`
- **Extension:** `.h`
- **Size:** 11167 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_keyagg_cache_save`
- `secp256k1_keyagg_cache_load`
- `secp256k1_musig_keyagglist_sha256`
- `secp256k1_musig_compute_pks_hash`
- `secp256k1_musig_keyaggcoef_sha256`
- `secp256k1_musig_keyaggcoef_internal`
- `secp256k1_musig_keyaggcoef`
- `secp256k1_musig_pubkey_agg_callback`
- `secp256k1_musig_pubkey_agg`
- `secp256k1_musig_pubkey_get`
- `secp256k1_musig_pubkey_tweak_add_internal`
- `secp256k1_musig_pubkey_ec_tweak_add`
- `secp256k1_musig_pubkey_xonly_tweak_add`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_MUSIG_KEYAGG_IMPL_H
#define SECP256K1_MODULE_MUSIG_KEYAGG_IMPL_H

#include <string.h>

#include "keyagg.h"
#include "../../eckey.h"
#include "../../ecmult.h"
#include "../../field.h"
#include "../../group.h"
#include "../../hash.h"
#include "../../util.h"

static const unsigned char secp256k1_musig_keyagg_cache_magic[4] = { 0xf4, 0xad, 0xbb, 0xdf };

...
```