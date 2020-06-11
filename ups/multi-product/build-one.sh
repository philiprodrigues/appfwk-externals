#!/bin/bash

set -eu

product=$1

if [ -z "$product" ]; then
    echo Usage: $(basename $0) project
    exit 1
fi


SRC_DIR=$HOME/cmake-ups/app-framework-externals/src
BUILD_DIR=$HOME/cmake-ups/app-framework-externals/build

set +eu
source  /cvmfs/larsoft.opensciencegrid.org/products/setup
if [ "$?" != "0" ]; then
    exit $?
fi
export PRODUCTS=$HOME/cmake-ups/products:$PRODUCTS
set -eu

mkdir -p ${BUILD_DIR}/$product
cd       ${BUILD_DIR}/$product

echo
echo '========================================================================'
echo Sourcing setup_for_development
# not really clear to me what this line does, but it's certainly
# necessary: it's creating some weird cet files that the cmake step
# depends on. I think '-p' is 'prof' qualifier, and the e19 has to
# match a qualifier in the ups/product_deps file
set +eu
source ${SRC_DIR}/${product}/ups/setup_for_development -p e19
if [ "$?" != "0" ]; then
    exit $?
fi
set -eu

echo
echo '========================================================================'
echo Running top-level cmake
# this command line is printed out by the previous step. the manual
# setting of CC and CXX appears to be necessary because of some checks
# done by the cet build scripts
env CC=gcc CXX=g++ FC=gfortran cmake -DCMAKE_INSTALL_PREFIX=$HOME/cmake-ups/products -DCMAKE_BUILD_TYPE=$CETPKG_TYPE ${SRC_DIR}/${product}

echo
echo '========================================================================'
echo Running make

make -j3

echo
echo '========================================================================'
echo Running make install

make install

echo
echo '========================================================================'
echo Running make package

make package
