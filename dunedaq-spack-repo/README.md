# Spack repository for appfwk and its dependencies

## Packages modified from the official spack distribution (folly and its dependencies):

* `double-conversion`: add new version
* `fmt`: add new version, build shared library
* `glog`: add new version
* `libevent`: add new version
* `folly`: add a new version, add `fmt` dependency. Now a `CMakePackage` instead of autotools
* `gflags`: add a new version, add patch to make shared library name match target name (hacky)

The situation with `folly`/`gflags` is fiddly, and I haven't worked out a good solution. I'm building `folly` with shared libraries, instead of static. `gflags` potentially builds several libraries; shared and static, and a "nothreads" version. For the shared library, a CMake target `gflags::gflags_shared` is exported, but the corresponding library name is `libgflags.so` (not `libgflags_shared.so`), set via the library target's `OUTPUT_NAME` property. The `folly` CMake scripts do some juggling to find the `gflags` library name, and assume that if a `gflags_shared` _target_ exists, then the corresponding _library_ name is `libgflags_shared.so`. Eventually this results in `folly's` "interface" libraries containing `gflags_shared` (which does not exist), and so applications that _depend_ on folly fail to build.

In the UPS product build, I worked around this by just not depending on `gflags`, which appears to be an optional dependency. A quick attempt to do this with spack resulted in a failed build, and in any case, the `folly` spack package depends on `glog` which itself depends on `gflags`. I think the correct solution is to fix the `folly` CMake scripts to look up the real library name from the `gflags_shared` target, or just to pass the actual target through to `libfolly`'s interface libraries.

## Packages modified from Fermilab spack repos:

* `cetlib`: change `catch2` dependency to not contain `~single_header`, since no such variant exists any more
* `cetlib-except`
* `cetmodules`
* `hep-concurrency`

I found these in the repository located at `/cvmfs/fermilab.opensciencegrid.org/packages/common/spack/rollout/NULL/var/spack/repos/fnal_art` which is a clone of the `https://cdcvs.fnal.gov/redmine/projects/spack-planning/repository/spack_art` git repo. There are no commits to `master` in that repo since Dec 2019 (but there are some on `feature/cetmodules_patches`, so I'm not sure what's up.

## Packages created for DUNE DAQ:

* `appfwk`
* `daq-buildtools`
* `ers`
* `trace`



