#!/bin/bash

set -ex

rm -rf public && hugo -D && rm -rf docs &&  mv public docs
