"""This script is run form setup.py (in the project root)"""

from __future__ import annotations

import os
from pathlib import Path

from cffi import FFI

repo_dir = Path(__file__).parent.parent.parent.parent.absolute()
src_dir = repo_dir / "src"
build_dir = repo_dir / "build"

cdefs = """
typedef struct handle_t {
  const void *_p;
  size_t _i;
} handle_t;

typedef struct handle_pair_t {
  handle_t first;
  handle_t second;
} handle_pair_t;

handle_t new_handle(size_t index);

handle_pair_t children(handle_t h);
"""

flags: dict[str, list[str]] = {}

flags["include_dirs"] = [str(src_dir)]

if os.name == "posix":
    flags["extra_link_args"] = [str(build_dir / "libfoo.a")]

# flags["extra_compile_args"] = ["-O2" if os.name != "nt" else "/O2"]
flags["extra_compile_args"] = ["-O0", "-g"]
# flags["extra_compile_args"] = ["-O0", "-g", "-fsanitize=address"]  # uncomment for address sanitizer

ffi = FFI()
ffi.set_source("_foo", "#include <foo.h>\n", ".c", **flags)
ffi.cdef(cdefs)

if __name__ == "__main__":
    ffi.compile(verbose=True)
