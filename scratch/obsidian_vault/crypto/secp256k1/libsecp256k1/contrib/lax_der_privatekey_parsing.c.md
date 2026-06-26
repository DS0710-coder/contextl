# lax_der_privatekey_parsing.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.c`
- **Extension:** `.c`
- **Size:** 5112 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ec_privkey_import_der`
- `ec_privkey_export_der`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.h.md|crypto/secp256k1/libsecp256k1/contrib/lax_der_privatekey_parsing.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2014, 2015 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#include <string.h>

#include "lax_der_privatekey_parsing.h"

int ec_privkey_import_der(const secp256k1_context* ctx, unsigned char *out32, const unsigned char *privkey, size_t privkeylen) {
    const unsigned char *end = privkey + privkeylen;
    int lenb = 0;
    int len = 0;
    memset(out32, 0, 32);
    /* sequence header */
    if (end < privkey+1 || *privkey != 0x30) {
        return 0;
    }
    privkey++;
...
```