# web3.js

## Architecture Metrics
- **Path:** `internal/jsre/deps/web3.js`
- **Extension:** `.js`
- **Size:** 394414 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `s`
- `Web3`
- `validateSingleMessage`
- `Eth`
- `Personal`
- `selectCipherStrategy`
- `xorBlock`
- `F`
- `parseLoop`
- `swapEndian`
- `FF`
- `GG`
- `HH`
- `II`
- `generateKeystreamAndEncrypt`
- `incWord`
- `incCounter`
- `nextState`
- `nextState`
- `generateKeystreamWord`
- `f1`
- `f2`
- `f3`
- `f4`
- `f5`
- `rotl`
- `isPrime`
- `getFractionalBits`
- `X64Word_create`
- `exchangeLR`
- `exchangeRL`
- `ucs2decode`
- `ucs2encode`
- `checkScalarValue`
- `createByte`
- `encodeCodePoint`
- `utf8encode`
- `readContinuationByte`
- `decodeSymbol`
- `utf8decode`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```js
require=(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
module.exports=[
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "name",
    "outputs": [
      {
        "name": "o_name",
        "type": "bytes32"
      }
    ],
    "type": "function"
  },
  {
...
```