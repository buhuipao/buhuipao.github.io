#!/bin/bash

set -ex

hugo -D && cd public && tar -cvf ../public.tar.gz . && cd -


HUGO_BRANCH=hugo
git push origin HEAD:$HUGO_BRANCH

REMOTE_URL=`git remote -v | grep push | head -n 1 | awk '{print $2}'`
REMOTE_BRANCH=main
git subtree push  --prefix=public $REMOTE_URL $REMOTE_BRANCH
