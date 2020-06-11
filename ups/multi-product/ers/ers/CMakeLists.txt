include(ExternalProject)

# We could just set the CMAKE_INSTALL_*DIR directories directly to
# ${CMAKE_INSTALL_PREFIX}/${ers_*_dir}, but we want to
# use CPack, which only knows about files/directories that are
# install()ed. So we install into a staging area and then install()
# from the staging area into the final destination
ExternalProject_Add (
  ers

  PREFIX         ers
  GIT_REPOSITORY https://github.com/philiprodrigues/ers
  GIT_TAG        dune/ers-00-26-00-cmake
  GIT_SHALLOW    ON

  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${PROJECT_BINARY_DIR}/external_staging
  CMAKE_ARGS     -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
                 -DCMAKE_INSTALL_LIBDIR:PATH=<INSTALL_DIR>/${ers_lib_dir}
                 -DCMAKE_INSTALL_BINDIR:PATH=<INSTALL_DIR>/${ers_bin_dir}
                 -DCMAKE_INSTALL_INCLUDEDIR:PATH=<INSTALL_DIR>/${ers_inc_dir}
                 -DBUILD_SHARED_LIBS=on
                 -DBoost_NO_BOOST_CMAKE=on -DBOOST_ROOT=$ENV{BOOST_FQ_DIR}
)

# The trailing / on the DIRECTORY argument acts like it does for
# cp. We need it to avoid double directories in the output. We have to
# use relative paths for the DESTINATION (which are interpreted as
# being relative to ${CMAKE_INSTALL_PREFIX}), so that CPack will work
message(STATUS "Going to install ${PROJECT_BINARY_DIR}/external_staging to ${CMAKE_INSTALL_PREFIX}")
install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/${ers_lib_dir}/
       DESTINATION ${ers_lib_dir})
install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/${ers_inc_dir}/
       DESTINATION ${ers_inc_dir})
install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/${ers_bin_dir}/
       DESTINATION ${ers_bin_dir})
