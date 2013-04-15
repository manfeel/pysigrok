from distutils.core import setup, Extension
import subprocess

sr_includes = subprocess.check_output(["pkg-config", "--cflags", "libsigrok"]).rstrip().split(' ')
sr_libs = subprocess.check_output(["pkg-config", "--libs", "libsigrok"]).rstrip().split(' ')

setup(
    name = 'sigrok',
    version = '0.1',
    description = "Sigrok API Wrapper",
    packages = ['sigrok'],
    ext_modules = [
        Extension('sigrok._libsigrok',
            sources = ['sigrok/libsigrok.i'],
            swig_opts = sr_includes,
            include_dirs = [i[2:] for i in sr_includes if i.startswith('-I')],
            library_dirs = [l[2:] for l in sr_libs if l.startswith('-L')],
            libraries = [l[2:] for l in sr_libs if l.startswith('-l')]
        )
    ],
)
