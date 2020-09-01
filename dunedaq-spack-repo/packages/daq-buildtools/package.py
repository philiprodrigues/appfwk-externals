# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install daq-buildtools
#
# You can edit this file again by typing:
#
#     spack edit daq-buildtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DaqBuildtools(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/philiprodrigues/daq-buildtools/archive/v1.1.1.tar.gz"
    git      = "https://github.com/philiprodrigues/daq-buildtools.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('spack-build', branch='spack-build')
    version('develop', branch='develop')
    version('1.1.1', sha256='541934fdfa8bb2937bf44d12173094525374e38ddd2dbfb43ce1c1e062ae5c19')
    version('1.1.2', sha256='4b478705bcd4ec23a078ca946ca8a3a35e98094ffdd5eb3f23ebdf0d5f00aa6f')
    version('1.1.3', sha256='ebc7703223b21d94ce66f46ffab9a425f49b545f8e06e65108e001fb0d5074c7')
    version('1.1.4', sha256='4e330230f850e0322885a2a602d121cacad1c390123d05b7c40b79a10ebba72a')
    version('1.1.5', sha256='dcf5345fbb2a3ffd6de029c58ea24fa261a53e7a6f67ae858d06619f1c701efd')
    version('1.1.6', sha256='1364ae589fc5484b4312893d9d5d278296e4403bd17649c4414f3547994640f4')
    
    def setup_dependent_build_environment(self, env, dependent_spec):
        env.append_path('CMAKE_MODULE_PATH', '{0}/lib64/cmake'
                        .format(self.prefix))

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.append_path('CMAKE_MODULE_PATH', '{0}/lib64/cmake'
                        .format(self.prefix))

    def setup_run_environment(self, env):
        env.append_path('CMAKE_MODULE_PATH', '{0}/lib64/cmake'
                        .format(self.prefix))

        
