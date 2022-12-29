from setuptools import setup

from mypyc.build import mypycify

setup(
    name="package",
    version="1.0",
    packages=["package"],
    ext_modules=mypycify(
        [
            "package/sub.py",
            "package/mod.py",
            "package/mod2.py",
        ]
    ),
)
