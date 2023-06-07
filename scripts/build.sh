#!/bin/bash

set -ex

hugo -D && cd public && tar -cvf ../public.tar.gz . && cd -



