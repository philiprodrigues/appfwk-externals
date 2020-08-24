# appfwk-externals
Code to build external packages for the [DUNE DAQ application framework](https://github.com/DUNE-DAQ/appfwk). This is designed for use on systems with CVMFS mounted, so only packages not available there are built. The current list of packages is:

* [ERS](https://github.com/DUNE-DAQ/ers)
* [folly](https://github.com/facebook/folly), and a (hopefully) minimal set of its dependencies:
  * [double-conversion](https://github.com/google/double-conversion)
  * [fmt](https://github.com/fmtlib/fmt)
  * [glog](https://github.com/google/glog)
  * [googletest](https://github.com/google/googletest)
  * [libevent](https://github.com/libevent/libevent)

Three methods of building the dependencies are included:

1. As regular cmake packages, using cmake's `ExternalProject`
2. As individual [UPS](https://cdcvs.fnal.gov/redmine/projects/ups/wiki/Getting_Started_Using_UPS) products, based on the template from [`cetbuildtools`](https://cdcvs.fnal.gov/redmine/projects/cetbuildtools/wiki)
3. As a [spack](https://spack.io/) repository

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

## Building the spack repository

This is currently (2020-08-24) fairly experimental, but worked in a test on the Fermilab interactive machines. Implementation notes and TODOs are in `dunedaq-spack-repo/README.md`.

The `dunedaq-spack-repo` directory contains a [spack](https://spack.io) repository, as described at https://spack.readthedocs.io/en/latest/repositories.html . Short instructions: add the repository to `repos.yaml`, make sure a sufficiently recent gcc is installed and known to spack (tested with 8.2.0), `spack install appfwk @develop %gcc@8.2.0`. In more detail:

The repository can be added to an existing spack installation by adding its path to `repos.yaml` in one of the [configuration scopes](https://spack.readthedocs.io/en/latest/configuration.html#configuration-scopes). For my tests, I added the repo to `~/.spack/linux/repos.yaml` like:

```yaml
repos:
- /dune/app/users/rodriges/dunedaq-spack-repo
- $spack/var/spack/repos/builtin
```

Scientific Linux 7's gcc is way too old. I built gcc 8.2.0 with spack using `spack install gcc@8.2.0`. To avoid waiting for the whole of gcc to build, you could install it from a [build cache](https://spack.readthedocs.io/en/latest/binary_caches.html). Make spack aware of the compiler via:

```bash
spack load gcc@8.2.0
spack compiler find `spack location --install-dir gcc@8.2.0`
```

With that in place, installing appfwk should just be a case of `spack install appfwk @develop %gcc@8.2.0`. Spack will collect, build and install `appfwk` and all of its dependencies. To activate appfwk in the current environment, run `spack load appfwk`.
