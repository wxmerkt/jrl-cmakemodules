#
# This file was generated by jrl-cmakemodules, do not modify
#

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from Cython.Build import cythonize

import hashlib
import os
import re

try:
    from numpy import get_include as numpy_get_include
except ImportError:
    def numpy_get_include():
        return ""

win32_build = os.name == 'nt'

sha512 = hashlib.sha512()
src_files = filter(len, '@CYTHON_BINDINGS_SOURCES@;@CYTHON_BINDINGS_GENERATE_SOURCES@'.split(';'))
def absolute(src):
    if os.path.isabs(src):
        return src
    else:
        return '{}/{}'.format('@CMAKE_CURRENT_SOURCE_DIR@', src)
src_files = map(absolute, src_files)
for f in src_files:
    chunk = 2**12
    with open(f, 'r') as fd:
        while True:
            data = fd.read(chunk)
            if data:
                sha512.update(data.encode('ascii'))
            else:
                break
version_hash = sha512.hexdigest()[:7]

class pkg_config(object):
    def __init__(self):
        compile_args = "@CYTHON_BINDINGS_COMPILE_DEFINITIONS@"
        self.compile_args = [ "-D" + x for x in compile_args.split(';') if len(x) ]
        self.compile_args = list(set(self.compile_args))
        include_dirs = "@CYTHON_BINDINGS_INCLUDE_DIRECTORIES@"
        include_dirs += ';{}'.format(numpy_get_include())
        self.include_dirs = [ x for x in include_dirs.split(';') if len(x) ]
        self.include_dirs.append('@CMAKE_CURRENT_SOURCE_DIR@/include')
        self.include_dirs = list(set(self.include_dirs))
        library_dirs = "@CYTHON_BINDINGS_LINK_FLAGS@"
        self.library_dirs = [ x for x in library_dirs.split(';') if len(x) ]
        self.libraries = [ re.sub("^lib", "", os.path.splitext(os.path.basename(l))[0]) for l in "@CYTHON_BINDINGS_LIBRARIES@".split(";") if len(l) ]
        self.libraries = list(set(self.libraries))
        self.library_dirs += [os.path.dirname(l) for l in "@CYTHON_BINDINGS_TARGET_FILES@".split(';') if len(l) ]
        self.library_dirs = list(set(self.library_dirs))
        self.link_args = []

config = pkg_config()

def cxx_standard(value):
    try:
        return int(value)
    except:
        return 0
def cxx_standard_cmp(lhs):
    if lhs == 98:
        return 1
    return lhs
cxx_standard = max(map(cxx_standard, "0;@CYTHON_BINDINGS_CXX_STANDARD@".split(';')), key = cxx_standard_cmp)
if cxx_standard != 0:
    if not win32_build:
        config.compile_args.append('-std=c++{}'.format(cxx_standard))
    else:
        if cxx_standard > 17:
            config.compile_args.append('/std:c++latest')
        elif cxx_standard == 17:
            config.compile_args.append('/std:c++17')

if win32_build:
    config.compile_args.append("-DWIN32")
    if "$<CONFIGURATION>".lower() == "debug":
        config.compile_args += ["-Zi", "/Od"]
        config.link_args += ["-debug"]

def GenExtension(name):
    pyx_src = name.replace('.', '/')
    pyx_src = pyx_src + '.pyx'
    ext_src = pyx_src
    return Extension(name, [ext_src], extra_compile_args = config.compile_args, include_dirs = config.include_dirs, library_dirs = config.library_dirs, libraries = config.libraries, extra_link_args = config.link_args)

extensions = [ GenExtension(x) for x in '@CYTHON_BINDINGS_MODULES@'.split(';') ]

extensions = cythonize(extensions)

packages = [ p.split('.')[0] for p in '@CYTHON_BINDINGS_MODULES@'.split(';') ]
package_data = { p : list(map(lambda x: x.replace(p + '/', ''), filter(lambda x: x.startswith(p + '/'), '@CYTHON_BINDINGS_EXPORT_SOURCES@'.split(';')))) for p in packages }

setup(
  name = '@CYTHON_BINDINGS_PACKAGE_NAME@',
  version='@CYTHON_BINDINGS_VERSION@-{}'.format(version_hash),
  ext_modules = extensions,
  packages = packages,
  package_data = package_data
)
