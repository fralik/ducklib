# Jammed version of Ducklib library

This repo intends to create a fake ducklib files modified to our needs.
In order to compile:

```dos
pip install cython~=0.29.16
python setup.py build_ext --inplace
```

We do not need to create the whole wheel package. We need individual files only.

## Test that library works

First, start duck-server in a separate terminal. Then:

```dos
pip install ducklib-1.0.0-cp37-cp37m-win_amd64.whl
python -c "import ducklib.main; ducklib.main.do_something()"
```