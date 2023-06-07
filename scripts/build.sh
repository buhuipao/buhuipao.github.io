#!/bin/bash

set -ex

hugo -D && mv public docs
