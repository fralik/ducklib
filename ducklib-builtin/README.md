# Compiled (builtin) version of Ducklib library

This repo is very similar to `ducklib-compiled` and differs only in the way how python code is compiled.
It results in functions that will have `builtin` type in Python.

**Note that you will need a working C++ compiler in order to work with this repo!**

In order to create the wheel do:

```dos
python setup.py bdist_wheel
```

Wheel shall be available in `dist` folder.

## Test that library works

First, start duck-server in a separate terminal. Then:

```dos
pip install ducklib_builtin-1.0.0-cp37-cp37m-win_amd64.whl
python -c "import ducklib.main; ducklib.main.do_something()"
```