# scratch_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scratch_impl.h`
- **Extension:** `.h`
- **Size:** 3677 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- ``
- `secp256k1_scratch_destroy`
- `secp256k1_scratch_checkpoint`
- `secp256k1_scratch_apply_checkpoint`
- `secp256k1_scratch_max_allocation`
- ``

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/scratch.h.md|crypto/secp256k1/libsecp256k1/src/scratch.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2017 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCRATCH_IMPL_H
#define SECP256K1_SCRATCH_IMPL_H

#include "util.h"
#include "scratch.h"

static secp256k1_scratch* secp256k1_scratch_create(const secp256k1_callback* error_callback, size_t size) {
    const size_t base_alloc = ROUND_TO_ALIGN(sizeof(secp256k1_scratch));
    void *alloc = checked_malloc(error_callback, base_alloc + size);
    secp256k1_scratch* ret = (secp256k1_scratch *)alloc;
    if (ret != NULL) {
        memset(ret, 0, sizeof(*ret));
        memcpy(ret->magic, "scratch", 8);
        ret->data = (void *) ((char *) alloc + base_alloc);
...
```