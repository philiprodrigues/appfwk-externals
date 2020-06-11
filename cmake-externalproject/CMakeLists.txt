cmake_minimum_required(VERSION 3.12)
project(app-framework-externals)

include(ExternalProject)

# BUILD_SHARED_LIBS=on allows us to find the ups boost install, which
# only has shared libraries (no static). (There might be a more
# boost-specific way to do this, TBD). That in turn makes folly want
# to build a shared library, which means everything needs -fPIC, which
# cmake spells CMAKE_POSITION_INDEPENDENT_CODE=on. The boost line is
# to force find_package(Boost ...) to use the cmake built-in
# boost-finding scripts, rather than the one that lives in the boost
# directory. The former is documented at
# https://cmake.org/cmake/help/latest/module/FindBoost.html and
# appears to be what folly is relying on. I can't actually find useful
# documentation for the latter

set(MY_CMAKE_ARGS
   -DBUILD_SHARED_LIBS:BOOL=ON
   -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
   -DCMAKE_PREFIX_PATH:PATH=<INSTALL_DIR>
   -DBoost_NO_BOOST_CMAKE=on -DBOOST_ROOT=$ENV{BOOST_FQ_DIR}
   -DCMAKE_POSITION_INDEPENDENT_CODE=on
   -DCMAKE_BUILD_TYPE=Release
)

ExternalProject_Add (
  double-conversion
  
  PREFIX         double-conversion
  GIT_REPOSITORY https://github.com/google/double-conversion
  GIT_TAG        v3.1.5
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}
  
  CMAKE_ARGS     ${MY_CMAKE_ARGS}
)

ExternalProject_Add (
  fmt
  
  PREFIX         fmt
  GIT_REPOSITORY https://github.com/fmtlib/fmt
  GIT_TAG        6.2.1
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}
  
  CMAKE_ARGS     ${MY_CMAKE_ARGS}
)

ExternalProject_Add (
  glog
  
  PREFIX         glog
  GIT_REPOSITORY https://github.com/google/glog
  GIT_TAG        v0.4.0
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}

  CMAKE_ARGS     ${MY_CMAKE_ARGS}  
)

ExternalProject_Add (
  googletest
  
  PREFIX         googletest
  GIT_REPOSITORY https://github.com/google/googletest
  GIT_TAG        release-1.8.1
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}
  
  CMAKE_ARGS     ${MY_CMAKE_ARGS}
)

ExternalProject_Add (
  libevent
  
  PREFIX         libevent
  GIT_REPOSITORY https://github.com/libevent/libevent
  GIT_TAG        release-2.1.8-stable
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}

  CMAKE_ARGS     ${MY_CMAKE_ARGS}  
)

ExternalProject_Add (
  ers
  
  PREFIX         ers
  GIT_REPOSITORY https://github.com/philiprodrigues/ers
  GIT_TAG        dune/ers-00-26-00-cmake
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}

  CMAKE_ARGS     ${MY_CMAKE_ARGS}  
)

ExternalProject_Add (
  folly
  
  PREFIX         folly
  GIT_REPOSITORY https://github.com/facebook/folly
  GIT_TAG        v2020.05.25.00
  GIT_SHALLOW    ON
  
  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${CMAKE_INSTALL_PREFIX}
  
  CMAKE_ARGS     ${MY_CMAKE_ARGS}

)

ExternalProject_Add_StepDependencies(folly download libevent)
ExternalProject_Add_StepDependencies(folly download double-conversion)
ExternalProject_Add_StepDependencies(folly download fmt)
ExternalProject_Add_StepDependencies(folly download glog)
ExternalProject_Add_StepDependencies(folly download googletest)
