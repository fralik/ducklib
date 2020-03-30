# Compiled version of Ducklib library

This repo mimics how one would created a library with compiled code ready for distribution.
In order to create the wheel do:

```dos
python setup.py bdist_wheel
```

Wheel shall be available in `dist` folder.

## Test that library works

First, start duck-server in a separate terminal. Then:

```dos
pip install ducklib-1.0.0-cp37-cp37m-win_amd64.whl
python -c "import ducklib.main; ducklib.main.do_something()"
```