include(ExternalProject)

# We could just set the CMAKE_INSTALL_*DIR directories directly to
# ${CMAKE_INSTALL_PREFIX}/${ers_*_dir}, but we want to
# use CPack, which only knows about files/directories that are
# install()ed. So we install into a staging area and then install()
# from the staging area into the final destination
ExternalProject_Add (
  nlohmann_json

  PREFIX         nlohmann_json
  GIT_REPOSITORY https://github.com/nlohmann/json
  GIT_TAG        v3.8.0
  GIT_SHALLOW    ON

  BUILD_ALWAYS   OFF
  INSTALL_DIR    ${PROJECT_BINARY_DIR}/external_staging
  CMAKE_ARGS     -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
                 -DBUILD_SHARED_LIBS=on
)

install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/lib64
       DESTINATION ${flavorqual_dir})
install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/include
       DESTINATION ${flavorqual_dir})
#install(DIRECTORY ${PROJECT_BINARY_DIR}/external_staging/bin
#       DESTINATION ${flavorqual_dir})
