import sysconfig

# The below import order is important. Do not change!
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from Cython.Build import cythonize

# Load the package's version number
about = {}
with open("src/ducklib/__version__.py") as fo:
    exec(fo.read(), about)


# noinspection PyPep8Naming
class build_py(_build_py):
    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            # a dirty way to omit .py files from .whl
            if 'auth' in filepath:
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules


setup(
    name="ducklib",
    version=about["__version__"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.7",
    ext_modules=cythonize("src/ducklib/auth*.py", compiler_directives={"language_level": "3"}, language="c++"),
    setup_requires=[
        "setuptools >= 18.0",
        "cython == 0.29.16",
    ],
    install_requires=[
        "requests ~= 2.23.0",
        "envparse ~= 0.2.0",
    ],
    extras_require={},
    package_data={},
    cmdclass={
        'build_py': build_py
    }
)
