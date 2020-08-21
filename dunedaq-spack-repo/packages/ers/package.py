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
#     spack install ers
#
# You can edit this file again by typing:
#
#     spack edit ers
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ers(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/DUNE-DAQ/ers"
    url      = "https://github.com/philiprodrigues/ers/archive/v1.0.1.tar.gz"

    version('1.0.0', sha256='ce793b721f27329c880304aec2fe48bf90fb8c4c9c34a4e25b8adb316d9e71a3')
    version('1.0.1', sha256='1e33adfad6e98eb9d4865afc61399fc8e844c9aa597d2b2c617f2735ea8cc9d4')

    depends_on('boost')
    
