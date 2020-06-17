# appfwk-externals
Code to build external packages for the [DUNE DAQ application framework](https://github.com/DUNE-DAQ/appfwk). This is designed for use on systems with CVMFS mounted, so only packages not available there are built. The current list of packages is:

* [ERS](https://github.com/DUNE-DAQ/ers)
* [folly](https://github.com/facebook/folly), and a (hopefully) minimal set of its dependencies:
  * [double-conversion](https://github.com/google/double-conversion)
  * [fmt](https://github.com/fmtlib/fmt)
  * [glog](https://github.com/google/glog)
  * [googletest](https://github.com/google/googletest)
  * [libevent](https://github.com/libevent/libevent)

Three methods of building the dependencies are included (although as of 2020-06-11, only the first actually works):

1. As regular cmake packages, using cmake's `ExternalProject`
2. As individual [UPS](https://cdcvs.fnal.gov/redmine/projects/ups/wiki/Getting_Started_Using_UPS) products, based on the template from [`cetbuildtools`](https://cdcvs.fnal.gov/redmine/projects/cetbuildtools/wiki)
3. As a single [UPS](https://cdcvs.fnal.gov/redmine/projects/ups/wiki/Getting_Started_Using_UPS) product which contains all of the dependencies

## Building as regular cmake packages

The code for this is in [cmake-externalproject](cmake-externalproject). Building it should be as simple as:

```bash
source setup.sh # if you want boost, cmake and gcc from cvmfs
cd an_appropriate_build_dir
cmake -DCMAKE_INSTALL_PREFIX=/path/to/install /path/to/cmake-externalproject
make && make install
```

If that succeeds, you'll have to point the app framework build at `/path/to/install` so it can find the dependencies. Adding `/path/to/install` to `$CMAKE_PREFIX_PATH` seems to do the trick.

## Building as individual UPS products

The individual UPS products are based on the template from [`cetbuildtools`](https://cdcvs.fnal.gov/redmine/projects/cetbuildtools/wiki), so the build procedure follows the method for that. You'll ned a local products directory: call it `$MYPRODUCTS`. Then, to build a product `$product`:

```bash
source /cvmfs/larsoft.opensciencegrid.org/products/setup # or wherever you get your gcc, boost ups products from
export PRODUCTS=$MYPRODUCTS:$PRODUCTS
source /path/to/appfwk-externals/ups/multi-product/${product}/ups/setup_for_development -p e19 # '-p' for profile, e19 is qualifier
cd /path/to/build/dir
env CC=gcc CXX=g++ FC=gfortran cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR -DCMAKE_BUILD_TYPE=$CETPKG_TYPE /path/to/appfwk-externals/ups/multi-product/$PRODUCT
make
make install
make package
```

It should now be possible to `setup` the product with ups as usual, eg via:
```bash
setup fmt v6_2_1 -q e19:prof
```

The `build-one.sh` script in `appfwk-externals/ups/multi-product` wraps the steps above. Call it as:

```bash
./build-one.sh $product /path/to/appfwk-externals/ups/multi-product/ /path/to/build/dir $MYPRODUCTS
```

and `build-all.sh` runs `build-one.sh` on all the products in an appropriate order. The arguments are the same, just without `$product`.
