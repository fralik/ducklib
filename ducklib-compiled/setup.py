from setuptools import setup, find_packages, Extension

# Load the package's version number
about = {}
with open("src/ducklib/__version__.py") as fo:
    exec(fo.read(), about)


ext_modules = [
    Extension(
        # such a name ensures, that compiled version is placed correctly in the wheel
        name='ducklib.auth',
        sources=["src/ducklib/auth.pyx"],
        # convert pyx to c++ code:
        language='c++',
    )
]

for e in ext_modules:
    if e.language == 'c++':
        e.cython_directives = {"language_level": "3"}

setup(
    name="ducklib",
    version=about["__version__"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.7",
    ext_modules=ext_modules,
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
)
