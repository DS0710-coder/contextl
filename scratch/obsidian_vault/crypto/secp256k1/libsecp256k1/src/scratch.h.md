# scratch.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scratch.h`
- **Extension:** `.h`
- **Size:** 2224 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_scratch_space_struct`
- `secp256k1_scratch_space_struct`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/scratch_impl.h.md|crypto/secp256k1/libsecp256k1/src/scratch_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2017 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCRATCH_H
#define SECP256K1_SCRATCH_H

/* The typedef is used internally; the struct name is used in the public API
 * (where it is exposed as a different typedef) */
typedef struct secp256k1_scratch_space_struct {
    /** guard against interpreting this object as other types */
    unsigned char magic[8];
    /** actual allocated data */
    void *data;
    /** amount that has been allocated (i.e. `data + offset` is the next
     *  available pointer)  */
    size_t alloc_size;
    /** maximum size available to allocate */
...
```