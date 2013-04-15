from distutils.core import setup, Extension
import subprocess

includes = subprocess.check_output(["pkg-config", "--cflags", "libsigrok"]).rstrip().split(' ')
libs = subprocess.check_output(["pkg-config", "--libs", "libsigrok"]).rstrip().split(' ')

setup(
    name = 'sigrok',
    version = '0.1',
    description = "Sigrok API Wrapper",
    packages = ['sigrok'],
    ext_modules = [
        Extension('sigrok._libsigrok',
            sources = ['sigrok/libsigrok.i'],
            extra_compile_args = includes + libs,
            swig_opts = includes
        )
    ],
)
