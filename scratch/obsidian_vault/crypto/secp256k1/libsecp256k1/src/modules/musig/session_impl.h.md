# session_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h`
- **Extension:** `.h`
- **Size:** 30954 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_musig_ge_serialize_ext`
- `secp256k1_musig_ge_parse_ext`
- `secp256k1_musig_secnonce_save`
- `secp256k1_musig_secnonce_load`
- `secp256k1_musig_secnonce_invalidate`
- `secp256k1_musig_pubnonce_save`
- `secp256k1_musig_pubnonce_load`
- `secp256k1_musig_aggnonce_save`
- `secp256k1_musig_aggnonce_load`
- `secp256k1_musig_session_save`
- `secp256k1_musig_session_load`
- `secp256k1_musig_partial_sig_save`
- `secp256k1_musig_partial_sig_load`
- `secp256k1_musig_pubnonce_parse`
- `secp256k1_musig_pubnonce_serialize`
- `secp256k1_musig_aggnonce_parse`
- `secp256k1_musig_aggnonce_serialize`
- `secp256k1_musig_partial_sig_parse`
- `secp256k1_musig_partial_sig_serialize`
- `secp256k1_nonce_function_musig_helper`
- `secp256k1_nonce_function_musig_sha256_tagged_aux`
- `secp256k1_nonce_function_musig_sha256_tagged`
- `secp256k1_nonce_function_musig`
- `secp256k1_musig_nonce_gen_internal`
- `secp256k1_musig_nonce_gen`
- `secp256k1_musig_nonce_gen_counter`
- `secp256k1_musig_sum_pubnonces`
- `secp256k1_musig_nonce_agg`
- `secp256k1_musig_compute_noncehash_sha256_tagged`
- `secp256k1_musig_compute_noncehash`
- `secp256k1_effective_nonce`
- `secp256k1_musig_nonce_process_internal`
- `secp256k1_musig_nonce_process`
- `secp256k1_musig_partial_sign_clear`
- `secp256k1_musig_partial_sign`
- `secp256k1_musig_partial_sig_verify`
- `secp256k1_musig_partial_sig_agg`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_MUSIG_SESSION_IMPL_H
#define SECP256K1_MODULE_MUSIG_SESSION_IMPL_H

#include <string.h>

#include "../../../include/secp256k1.h"
#include "../../../include/secp256k1_extrakeys.h"
#include "../../../include/secp256k1_musig.h"

#include "keyagg.h"
#include "session.h"
#include "../../eckey.h"
#include "../../hash.h"
#include "../../scalar.h"
#include "../../util.h"
...
```