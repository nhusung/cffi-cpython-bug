# CFFI/CPython Bug Reproducibility Package

0. Create a virtualenv if desired (`python3 -m venv .venv; source .venv/bin/activate`)
1. Run `make` to build the C library
2. Run `pip install --editable .` to build and install the Python module
3. Execute the test via `python3 -c 'import foo'`

In order to compile and run the Python module with the address sanitizer enabled, you would need to

1. Install `libasan` (the package is called `libasan8` on Ubuntu and `libasan` on Fedora)
2. Uncomment the respective line in `bindings/python/build/ffi.py`
3. Run `pip install --editable .` again
4. Execute `LD_PRELOAD=/path/to/libasan.so.x python3 -c 'import foo'` (on Ubuntu, `libasan` is installed at `/usr/lib/x86_64-linux-gnu/libasan.so.8`, on Fedora it is at `/usr/lib64/libasan.so.8`)
