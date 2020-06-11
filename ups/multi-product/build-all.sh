#!/bin/bash

set -eu

for i in ers fmt glog googletest double_conversion libevent folly; do
    ./build-one.sh $i 2>&1 | tee ${i}-build.log 2>&1 || exit 1
done
