# tests.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/tests.c`
- **Extension:** `.c`
- **Size:** 366322 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 19

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test_hsort_cmp_data`
- `test_hsort_cmp_data`
- `test_hsort_cmp_data`
- `test_hsort_cmp_data`
- `all_bytes_equal`
- `counting_callback_fn`
- `uncounting_illegal_callback_fn`
- `run_xoshiro256pp_tests`
- `run_selftest_tests`
- `ecmult_gen_context_eq`
- `context_eq`
- `run_deprecated_context_flags_test`
- `run_ec_illegal_argument_tests`
- `run_static_context_tests`
- `run_proper_context_tests`
- `run_scratch_tests`
- `run_ctz_tests`
- `run_sha256_known_output_tests`
- `run_sha256_counter_tests`
- `test_sha256_eq`
- `run_hmac_sha256_tests`
- `run_rfc6979_hmac_sha256_tests`
- `run_tagged_sha256_tests`
- `modinv2p64`
- `mulmod256`
- `uint16_to_signed30`
- `signed30_to_uint16`
- `mutate_sign_signed30`
- `test_modinv32_uint16`
- `uint16_to_signed62`
- `signed62_to_uint16`
- `mutate_sign_signed62`
- `test_modinv64_uint16`
- `coprime`
- `run_modinv_tests`
- `add256`
- `neg256`
- `rshift256`
- `load256u64`
- `load256two64`
- `int256is127`
- `load256u128`
- `load256i128`
- `run_int128_test_case`
- `run_int128_tests`
- `scalar_test`
- `run_scalar_set_b32_seckey_tests`
- `run_scalar_tests`
- `random_fe_non_square`
- `fe_equal`
- `run_field_convert`
- `run_field_be32_overflow`
- `fe_identical`
- `run_field_half`
- `run_field_misc`
- `test_fe_mul`
- `run_fe_mul`
- `run_sqr`
- `test_sqrt`
- `run_sqrt`
- `test_inverse_scalar`
- `test_inverse_field`
- `run_inverse_tests`
- `test_heap_swap`
- `test_hsort_is_sorted`
- `test_hsort_cmp`
- `test_hsort`
- `run_hsort_tests`
- `gej_xyz_equals_gej`
- `test_ge`
- `test_intialized_inf`
- `test_add_neg_y_diff_x`
- `test_ge_bytes`
- `run_ge`
- `test_gej_cmov`
- `run_gej`
- `test_ec_combine`
- `run_ec_combine`
- `test_group_decompress`
- `run_group_decompress`
- `test_pre_g_table`
- `run_ecmult_pre_g`
- `run_ecmult_chain`
- `test_point_times_order`
- `test_ecmult_target`
- `run_ecmult_near_split_bound`
- `run_point_times_order`
- `ecmult_const_random_mult`
- `ecmult_const_commutativity`
- `ecmult_const_mult_zero_one`
- `ecmult_const_check_result`
- `ecmult_const_edges`
- `ecmult_const_mult_xonly`
- `ecmult_const_chain_multiply`
- `run_ecmult_const_tests`
- `ecmult_multi_callback`
- `ecmult_multi_false_callback`
- `test_ecmult_multi`
- `test_ecmult_multi_random`
- `test_ecmult_multi_batch_single`
- `test_secp256k1_pippenger_bucket_window_inv`
- `test_ecmult_multi_pippenger_max_points`
- `test_ecmult_multi_batch_size_helper`
- `test_ecmult_multi_batching`
- `run_ecmult_multi_tests`
- `test_wnaf`
- `test_fixed_wnaf`
- `test_fixed_wnaf_small_helper`
- `test_fixed_wnaf_small`
- `run_wnaf`
- `test_ecmult_accumulate_cb`
- `test_ecmult_accumulate`
- `test_ecmult_constants_2bit`
- `test_ecmult_constants_sha`
- `run_ecmult_constants`
- `test_ecmult_gen_blind`
- `test_ecmult_gen_blind_reset`
- `test_ecmult_gen_edge_cases`
- `run_ecmult_gen_blind`
- `test_scalar_split`
- `run_endomorphism_tests`
- `ec_pubkey_parse_pointtest`
- `run_ec_pubkey_parse_test`
- `run_eckey_edge_case_test`
- `run_eckey_negate_test`
- `random_sign`
- `test_ecdsa_sign_verify`
- `run_ecdsa_sign_verify`
- `precomputed_nonce_function`
- `nonce_function_test_fail`
- `nonce_function_test_retry`
- `is_empty_signature`
- `test_ecdsa_end_to_end`
- `test_random_pubkeys`
- `run_pubkey_comparison`
- `test_sort_helper`
- `permute`
- `test_sort_api`
- `test_sort`
- `test_sort_vectors`
- `run_pubkey_sort`
- `run_random_pubkeys`
- `run_ecdsa_end_to_end`
- `test_ecdsa_der_parse`
- `assign_big_endian`
- `damage_array`
- `random_ber_signature`
- `run_ecdsa_der_parse`
- `test_ecdsa_edge_cases`
- `run_ecdsa_edge_cases`
- `test_ecdsa_wycheproof`
- `run_ecdsa_wycheproof`
- `run_secp256k1_memczero_test`
- `run_secp256k1_is_zero_array_test`
- `run_secp256k1_byteorder_tests`
- `int_cmov_test`
- `fe_cmov_test`
- `fe_storage_cmov_test`
- `scalar_cmov_test`
- `ge_storage_cmov_test`
- `run_cmov_tests`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/contrib/lax_der_parsing.c.md|crypto/secp256k1/libsecp256k1/contrib/lax_der_parsing.c]]
- [[crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.c.md|crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.c]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h]]
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv32_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv64_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv64_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/testrand_impl.h.md|crypto/secp256k1/libsecp256k1/src/testrand_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/testutil.h.md|crypto/secp256k1/libsecp256k1/src/testutil.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]
- [[crypto/secp256k1/libsecp256k1/src/wycheproof/ecdsa_secp256k1_sha256_bitcoin_test.h.md|crypto/secp256k1/libsecp256k1/src/wycheproof/ecdsa_secp256k1_sha256_bitcoin_test.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2013, 2014, 2015 Pieter Wuille, Gregory Maxwell       *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <time.h>

#ifdef USE_EXTERNAL_DEFAULT_CALLBACKS
    #pragma message("Ignoring USE_EXTERNAL_CALLBACKS in tests.")
    #undef USE_EXTERNAL_DEFAULT_CALLBACKS
#endif
#if defined(VERIFY) && defined(COVERAGE)
    #pragma message("Defining VERIFY for tests being built for coverage analysis support is meaningless.")
#endif
#include "secp256k1.c"
...
```