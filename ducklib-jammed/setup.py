# The below import order is important. Do not change!
from setuptools import setup, find_packages
from Cython.Build import cythonize

# Load the package's version number
about = {}
with open("src/ducklib/__version__.py") as fo:
    exec(fo.read(), about)


setup(
    name="ducklib",
    version=about["__version__"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.7",
    ext_modules=cythonize("src/ducklib/auth.py", compiler_directives={"language_level": "3"}, language="c++"),
    setup_requires=[
        "setuptools >= 18.0",
        "cython == 0.29.16",
    ],
    install_requires=[
    ],
    extras_require={},
    package_data={},
)
