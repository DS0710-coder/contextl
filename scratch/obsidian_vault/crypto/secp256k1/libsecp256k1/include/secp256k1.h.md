# secp256k1.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1.h`
- **Extension:** `.h`
- **Size:** 42445 bytes
- **Centrality Score:** 0.0085
- **In-Degree (Imported By):** 30
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_context_struct`
- `secp256k1_pubkey`
- `secp256k1_ecdsa_signature`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/contrib/lax_der_parsing.h.md|crypto/secp256k1/libsecp256k1/contrib/lax_der_parsing.h]]
- [[crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.h.md|crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.h]]
- [[crypto/secp256k1/libsecp256k1/examples/ecdh.c.md|crypto/secp256k1/libsecp256k1/examples/ecdh.c]]
- [[crypto/secp256k1/libsecp256k1/examples/ecdsa.c.md|crypto/secp256k1/libsecp256k1/examples/ecdsa.c]]
- [[crypto/secp256k1/libsecp256k1/examples/ellswift.c.md|crypto/secp256k1/libsecp256k1/examples/ellswift.c]]
- [[crypto/secp256k1/libsecp256k1/examples/musig.c.md|crypto/secp256k1/libsecp256k1/examples/musig.c]]
- [[crypto/secp256k1/libsecp256k1/examples/schnorr.c.md|crypto/secp256k1/libsecp256k1/examples/schnorr.c]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_preallocated.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_H
#define SECP256K1_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>

/** Unless explicitly stated all pointer arguments must not be NULL.
 *
 * The following rules specify the order of arguments in API calls:
 *
 * 1. Context pointers go first, followed by output arguments, combined
 *    output/input arguments, and finally input-only arguments.
 * 2. Array lengths always immediately follow the argument whose length
 *    they describe, even if this violates rule 1.
 * 3. Within the OUT/OUTIN/IN groups, pointers to data that is typically generated
 *    later go first. This means: signatures, public nonces, secret nonces,
 *    messages, public keys, secret keys, tweaks.
...
```