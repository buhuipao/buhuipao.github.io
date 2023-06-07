#!/bin/bash

set -ex

hugo -D && rm -rf docs &&  mv public docs
