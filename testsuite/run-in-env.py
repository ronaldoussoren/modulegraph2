#!/usr/bin/env python3.11

import importlib
import runpy
import sys

env_root = sys.argv[1]

activate_this = f"{env_root}/bin/activate_this.py"
with open(activate_this, "rb") as stream:
    activate_source = stream.read()

exec(activate_source, {"__file__": activate_this})
importlib.invalidate_caches()

sys.argv[:] = "coverage run --parallel -m unittest -v".split()
runpy.run_module("coverage")
