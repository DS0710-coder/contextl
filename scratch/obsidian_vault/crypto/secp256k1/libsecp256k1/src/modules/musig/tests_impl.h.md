# tests_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h`
- **Extension:** `.h`
- **Size:** 58541 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 11

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `musig_key_agg_vector`
- `musig_key_agg_valid_test_case`
- `musig_key_agg_error_test_case`
- `musig_nonce_gen_vector`
- `musig_nonce_gen_test_case`
- `musig_nonce_agg_vector`
- `musig_nonce_agg_test_case`
- `musig_nonce_agg_test_case`
- `musig_sign_verify_vector`
- `musig_valid_case`
- `musig_sign_error_case`
- `musig_verify_fail_error_case`
- `musig_verify_fail_error_case`
- `musig_tweak_vector`
- `musig_tweak_case`
- `musig_tweak_case`
- `musig_sig_agg_vector`
- `musig_sig_agg_case`
- `musig_sig_agg_case`
- `create_keypair_and_pk`
- `musig_simple_test`
- `pubnonce_summing_to_inf`
- `memcmp_and_randomize`
- `musig_api_tests`
- `musig_nonce_bitflip`
- `musig_nonce_test`
- `sha256_tag_test_internal`
- `sha256_tag_test`
- `musig_tweak_test_helper`
- `musig_tweak_test`
- `musig_vectors_keyagg_and_tweak`
- `musig_test_vectors_keyagg`
- `musig_test_vectors_noncegen`
- `musig_test_vectors_nonceagg`
- `musig_test_set_secnonce`
- `musig_test_vectors_signverify`
- `musig_test_vectors_tweak`
- `musig_test_vectors_sigagg`
- `musig_test_static_nonce_gen_counter`
- `run_musig_tests`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/vectors.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/vectors.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_MUSIG_TESTS_IMPL_H
#define SECP256K1_MODULE_MUSIG_TESTS_IMPL_H

#include <stdlib.h>
#include <string.h>

#include "../../../include/secp256k1.h"
#include "../../../include/secp256k1_extrakeys.h"
#include "../../../include/secp256k1_musig.h"

#include "session.h"
#include "keyagg.h"
#include "../../scalar.h"
#include "../../field.h"
#include "../../group.h"
...
```