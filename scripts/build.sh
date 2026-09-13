#!/bin/bash

set -ex

# Allow overriding baseURL via environment variable for multi-deploy setups
# Usage:
#   HUGO_BASEURL="https://example.com/" bash -ex scripts/build.sh

rm -rf public
hugo --baseURL "${HUGO_BASEURL:-https://buhuipao.github.io/}"
rm -rf docs
mv public docs
