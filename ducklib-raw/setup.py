from setuptools import setup, find_packages

# Load the package's version number
about = {}
with open("src/ducklib/__version__.py") as fo:
    exec(fo.read(), about)

setup(
    name="ducklib",
    version=about["__version__"],
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires="~=3.7",
    install_requires=[
        "requests ~= 2.23.0",
        "envparse ~= 0.2.0"
    ],
    extras_require={
    },
    package_data={},
)
