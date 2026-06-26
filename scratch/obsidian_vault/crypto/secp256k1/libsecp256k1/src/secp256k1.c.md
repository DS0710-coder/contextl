# secp256k1.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/secp256k1.c`
- **Extension:** `.c`
- **Size:** 29389 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 24

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_context_struct`
- `secp256k1_context_is_proper`
- `secp256k1_selftest`
- `secp256k1_context_preallocated_size`
- `secp256k1_context_preallocated_clone_size`
- ``
- ``
- ``
- ``
- `secp256k1_context_preallocated_destroy`
- `secp256k1_context_destroy`
- `secp256k1_context_set_illegal_callback`
- `secp256k1_context_set_error_callback`
- ``
- `secp256k1_scratch_space_destroy`
- `secp256k1_declassify`
- `secp256k1_pubkey_load`
- `secp256k1_pubkey_save`
- `secp256k1_ec_pubkey_parse`
- `secp256k1_ec_pubkey_serialize`
- `secp256k1_ec_pubkey_cmp`
- `secp256k1_ec_pubkey_sort_cmp`
- `secp256k1_ec_pubkey_sort`
- `secp256k1_ecdsa_signature_load`
- `secp256k1_ecdsa_signature_save`
- `secp256k1_ecdsa_signature_parse_der`
- `secp256k1_ecdsa_signature_parse_compact`
- `secp256k1_ecdsa_signature_serialize_der`
- `secp256k1_ecdsa_signature_serialize_compact`
- `secp256k1_ecdsa_signature_normalize`
- `secp256k1_ecdsa_verify`
- `buffer_append`
- `nonce_function_rfc6979`
- `secp256k1_ecdsa_sign_inner`
- `secp256k1_ecdsa_sign`
- `secp256k1_ec_seckey_verify`
- `secp256k1_ec_pubkey_create_helper`
- `secp256k1_ec_pubkey_create`
- `secp256k1_ec_seckey_negate`
- `secp256k1_ec_privkey_negate`
- `secp256k1_ec_pubkey_negate`
- `secp256k1_ec_seckey_tweak_add_helper`
- `secp256k1_ec_seckey_tweak_add`
- `secp256k1_ec_privkey_tweak_add`
- `secp256k1_ec_pubkey_tweak_add_helper`
- `secp256k1_ec_pubkey_tweak_add`
- `secp256k1_ec_seckey_tweak_mul`
- `secp256k1_ec_privkey_tweak_mul`
- `secp256k1_ec_pubkey_tweak_mul`
- `secp256k1_context_randomize`
- `secp256k1_ec_pubkey_combine`
- `secp256k1_tagged_sha256`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey_impl.h.md|crypto/secp256k1/libsecp256k1/src/eckey_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash_impl.h.md|crypto/secp256k1/libsecp256k1/src/hash_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/hsort_impl.h.md|crypto/secp256k1/libsecp256k1/src/hsort_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scratch_impl.h.md|crypto/secp256k1/libsecp256k1/src/scratch_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/selftest.h.md|crypto/secp256k1/libsecp256k1/src/selftest.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2013-2015 Pieter Wuille                               *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

/* This is a C project. It should not be compiled with a C++ compiler,
 * and we error out if we detect one.
 *
 * We still want to be able to test the project with a C++ compiler
 * because it is still good to know if this will lead to real trouble, so
 * there is a possibility to override the check. But be warned that
 * compiling with a C++ compiler is not supported. */
#if defined(__cplusplus) && !defined(SECP256K1_CPLUSPLUS_TEST_OVERRIDE)
#error Trying to compile a C project with a C++ compiler.
#endif

#define SECP256K1_BUILD

#include "../include/secp256k1.h"
...
```