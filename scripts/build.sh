#!/bin/bash

set -ex

# Allow overriding baseURL via environment variable for multi-deploy setups
# Usage:
#   HUGO_BASEURL="https://example.com/" bash -ex scripts/build.sh

BASEURL_FLAG=""
if [ -n "${HUGO_BASEURL:-}" ]; then
  BASEURL_FLAG="-b ${HUGO_BASEURL}"
fi

rm -rf public
hugo -D ${BASEURL_FLAG}
rm -rf docs
mv public docs
