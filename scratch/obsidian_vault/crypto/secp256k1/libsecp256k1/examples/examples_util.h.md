# examples_util.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/examples/examples_util.h`
- **Extension:** `.h`
- **Size:** 4479 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `fill_random`
- `print_hex`
- `secure_erase`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/ecdh.c.md|crypto/secp256k1/libsecp256k1/examples/ecdh.c]]
- [[crypto/secp256k1/libsecp256k1/examples/ecdsa.c.md|crypto/secp256k1/libsecp256k1/examples/ecdsa.c]]
- [[crypto/secp256k1/libsecp256k1/examples/ellswift.c.md|crypto/secp256k1/libsecp256k1/examples/ellswift.c]]
- [[crypto/secp256k1/libsecp256k1/examples/musig.c.md|crypto/secp256k1/libsecp256k1/examples/musig.c]]
- [[crypto/secp256k1/libsecp256k1/examples/schnorr.c.md|crypto/secp256k1/libsecp256k1/examples/schnorr.c]]

## Source Code Snippet
```h
/*************************************************************************
 * Copyright (c) 2020-2021 Elichai Turkel                                *
 * Distributed under the CC0 software license, see the accompanying file *
 * EXAMPLES_COPYING or https://creativecommons.org/publicdomain/zero/1.0 *
 *************************************************************************/

/*
 * This file is an attempt at collecting best practice methods for obtaining randomness with different operating systems.
 * It may be out-of-date. Consult the documentation of the operating system before considering to use the methods below.
 *
 * Platform randomness sources:
 * Linux   -> `getrandom(2)`(`sys/random.h`), if not available `/dev/urandom` should be used. http://man7.org/linux/man-pages/man2/getrandom.2.html, https://linux.die.net/man/4/urandom
 * macOS   -> `getentropy(2)`(`sys/random.h`), if not available `/dev/urandom` should be used. https://www.unix.com/man-page/mojave/2/getentropy, https://opensource.apple.com/source/xnu/xnu-517.12.7/bsd/man/man4/random.4.auto.html
 * FreeBSD -> `getrandom(2)`(`sys/random.h`), if not available `kern.arandom` should be used. https://www.freebsd.org/cgi/man.cgi?query=getrandom, https://www.freebsd.org/cgi/man.cgi?query=random&sektion=4
 * OpenBSD -> `getentropy(2)`(`unistd.h`), if not available `/dev/urandom` should be used. https://man.openbsd.org/getentropy, https://man.openbsd.org/urandom
 * Windows -> `BCryptGenRandom`(`bcrypt.h`). https://docs.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom
 */

#if defined(_WIN32)
/*
...
```