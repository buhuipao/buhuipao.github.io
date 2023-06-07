#!/bin/bash

set -ex

hugo -D && cd public && tar -cvf ../public.tar.gz . && cd -

git subtree push  --prefix=public git@github.com:buhuipao/buhuipao.github.io.git main
