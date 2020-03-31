# Compiled version of Ducklib library

This repo mimics how one would created a library with compiled code ready for distribution.

**Note that you will need a working C++ compiler in order to work with this repo!**


In order to create the wheel do:

```dos
py -3.7 -m venv ./venv --prompt ducklib-compiled-dev
./venv/scripts/acrivate
python -m pip install --upgrade setuptools wheel pip
pip install cython~=0.29.16
python setup.py bdist_wheel
```

Wheel shall be available in `dist` folder.

## Test that library works

First, start duck-server in a separate terminal. Then:

```dos
pip install ducklib-1.0.0-cp37-cp37m-win_amd64.whl
python -c "import ducklib.main; ducklib.main.do_something()"
```