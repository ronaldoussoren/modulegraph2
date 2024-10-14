"""
Some useful utility functions.
"""

import contextlib
import importlib
import pathlib
import sys
from typing import List, Optional, Tuple


@contextlib.contextmanager
def saved_sys_path():
    """
    Contextmanager that will restore the value
    of :data:`sys.path` when leaving the ``with``
    block.
    """
    orig_path = list(sys.path)

    try:
        yield

    finally:
        sys.path[:] = orig_path
        importlib.invalidate_caches()


def split_package(name: str) -> Tuple[Optional[str], str]:
    """
    Return (package, name) given a fully qualified module name

    package is ``None`` for toplevel modules
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected 'str', got instance of {type(name)!r}")
    if not name:
        raise ValueError(f"Invalid module name {name!r}")

    name_abs = name.lstrip(".")
    dots = len(name) - len(name_abs)
    if not name_abs or ".." in name_abs:
        raise ValueError(f"Invalid module name {name!r}")

    package, _, name = name_abs.rpartition(".")
    if dots:
        package = ("." * dots) + package

    return (package if package != "" else None), name


class FakePackage:
    """
    Instances of these can be used to represent a fake
    package in :data:`sys.modules`.

    Used as a workaround to fetch information about modules
    in packages when the package itself cannot be imported
    for some reason (for example due to having a SyntaxError
    in the module ``__init__.py`` file).
    """

    def __init__(self, path: List[str]):
        """
        Create a new instance.

        Args:
           path: The search path for sub modules
        """
        self.__path__ = path


if hasattr(sys, "stdlib_module_names"):

    def stdlib_module_names() -> List[str]:
        """
        Return a list of modules in the standard library
        """
        return list(sys.stdlib_module_names)  # type: ignore

else:

    def stdlib_module_names() -> List[str]:
        """
        Return a list of modules in the standard library
        """
        # Alternative implementation for Python 3.9 or earlier
        # that do not have sys.stdlib_module_names. The implementation
        # can fail for frozen applications.
        import sysconfig

        result = list(sys.builtin_module_names)

        prefix = pathlib.Path(sysconfig.get_paths()["stdlib"])
        for p in prefix.iterdir():
            if p.suffix == ".py":
                result.append(p.stem)
            elif p.is_dir() and p.name.isidentifier():
                result.append(p.name)

        return result
