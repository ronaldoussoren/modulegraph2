import distutils
import os
import pathlib
import sys
import unittest

import modulegraph2
from modulegraph2 import _virtualenv_support as virtualenv_support

PYLIB_DIR = f"python{sys.version_info[0]}.{sys.version_info[1]}"

if hasattr(sys, "real_prefix"):

    class TestUtilities(unittest.TestCase):
        def test_same_contents(self):
            self.assertTrue(virtualenv_support.same_contents(__file__, __file__))

            self.assertFalse(
                virtualenv_support.same_contents(
                    __file__, pathlib.Path(__file__).parent / "test_mypyc_support.py"
                )
            )

        def test_same_contents_fails(self):
            with self.assertRaises(FileNotFoundError):
                virtualenv_support.same_contents(__file__, "no-such-file.txt")

            with self.assertRaises(FileNotFoundError):
                virtualenv_support.same_contents("no-such-file.txt", __file__)

    class TestAdjustPath(unittest.TestCase):
        def test_stdlib(self):
            import token

            adjusted = virtualenv_support.adjust_path(token.__file__)
            self.assertEqual(
                adjusted, os.path.join(sys.base_prefix, "lib", PYLIB_DIR, "token.py")
            )

        def test_stdlib_extension(self):
            import cmath

            adjusted = virtualenv_support.adjust_path(cmath.__file__)
            self.assertEqual(
                adjusted,
                os.path.join(
                    sys.base_prefix,
                    "lib",
                    PYLIB_DIR,
                    "lib-dynload",
                    os.path.basename(cmath.__file__),
                ),
            )

        @unittest.skipIf("_distutils" in distutils.__file__, "modern setuptools")
        def test_distutils(self):
            import distutils

            print(distutils.__file__)

            adjusted = virtualenv_support.adjust_path(distutils.__file__)
            self.assertEqual(
                adjusted,
                os.path.join(
                    sys.real_prefix, "lib", PYLIB_DIR, "distutils", "__init__.py"
                ),
            )

            distutils_dir = os.path.dirname(distutils.__file__)
            adjusted = virtualenv_support.adjust_path(distutils_dir)
            self.assertEqual(
                adjusted, os.path.join(sys.real_prefix, "lib", PYLIB_DIR, "distutils")
            )

        def test_site(self):
            import site

            adjusted = virtualenv_support.adjust_path(site.__file__)
            self.assertEqual(
                adjusted, os.path.join(sys.base_prefix, "lib", PYLIB_DIR, "site.py")
            )

        def test_site_packages(self):
            import pip

            adjusted = virtualenv_support.adjust_path(pip.__file__)
            self.assertEqual(adjusted, pip.__file__)

        def test_other_path_in_env(self):
            self.assertEqual(
                virtualenv_support.adjust_path(sys.executable), sys.executable
            )

            path = os.path.join(sys.prefix, "lib", PYLIB_DIR, "foo.py")
            self.assertEqual(virtualenv_support.adjust_path(path), path)

        def test_system_path(self):
            path = "/etc"
            self.assertEqual(virtualenv_support.adjust_path(path), path)

        def test_site_packages2(self):
            site_path = os.path.join(virtualenv_support.site_packages, "link.file")
            adjusted = virtualenv_support.adjust_path(site_path)
            self.assertEqual(adjusted, site_path)

        def test_site_py(self):
            adjusted = virtualenv_support.adjust_path(
                os.path.join(virtualenv_support.virtual_lib, "site.py")
            )
            self.assertEqual(
                adjusted, os.path.join(virtualenv_support.real_lib, "site.py")
            )

        @unittest.skipIf(sys.platform == "win32", "not relevant on windowws")
        def test_norm_symlink(self):
            site_path = os.path.join(virtualenv_support.virtual_lib, "link.file")
            os.symlink("/etc/no-such-file.txt", site_path)
            try:
                self.assertEqual(
                    virtualenv_support.adjust_path(site_path), "/etc/no-such-file.txt"
                )
            finally:
                os.unlink(site_path)

            site_path = os.path.join(virtualenv_support.virtual_lib, "link.file")
            os.symlink(sys.base_prefix, site_path)
            try:
                self.assertEqual(
                    virtualenv_support.adjust_path(os.path.join(site_path, "lib")),
                    os.path.join(sys.base_prefix, "lib"),
                )
            finally:
                os.unlink(site_path)

    class TestAdjustUsage(unittest.TestCase):
        @unittest.skipIf("_distutils" in distutils.__file__, "modern setuptools")
        def test_adjustments(self):
            # Explicitly test adjustments for distutils because virtualenv environments
            # contain a stub distutils package that should not be present in the graph.
            mg = modulegraph2.ModuleGraph()
            mg.add_module("distutils.command.build_ext")

            node = mg.find_node("distutils")
            self.assertIsInstance(node, modulegraph2.Package)
            self.assertIsInstance(node.init_module, modulegraph2.SourceModule)

            self.assertEqual(
                node.init_module.filename,
                pathlib.Path(sys.base_prefix)
                / "lib"
                / PYLIB_DIR
                / "distutils"
                / "__init__.py",
            )
