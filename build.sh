#!/bin/bash
set -e

echo "Building npm package..."
rm -rf npm/python
mkdir -p npm/python
cp src/*.py npm/python/

echo "Building PyPI package..."
rm -rf pypi/python
mkdir -p pypi/python
cp src/*.py pypi/python/

echo "Done. Run 'cd npm && npm publish' or 'cd pypi && python -m build' next."
