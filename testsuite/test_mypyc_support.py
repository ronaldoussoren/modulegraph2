import contextlib
import importlib
import os
import pathlib
import shutil
import sys
import tempfile
import unittest

import modulegraph2

from . import util
from .test_distributions import build_and_install

INPUT_DIR = pathlib.Path(__file__).resolve().parent / "mypyc-dir"


@contextlib.contextmanager
def prefixed_sys_path(dir_path):
    sys.path.insert(0, os.fspath(dir_path))
    try:
        yield

    finally:
        assert sys.path[0] == os.fspath(dir_path)
        del sys.path[0]
        util.clear_sys_modules(dir_path)


class TestMypycSupport(unittest.TestCase):
    def setUp(self):
        self._modules = sys.modules.copy()

    def tearDown(self):
        util.clear_sys_modules(INPUT_DIR)
        sys.modules.clear()
        sys.modules.update(self._modules)
        importlib.invalidate_caches()

    @classmethod
    def tearDownClass(cls):
        util.clear_sys_modules(INPUT_DIR)

        for subdir in INPUT_DIR.iterdir():
            if not subdir.is_dir():
                continue

            if (subdir / "build").exists():
                shutil.rmtree(subdir / "build")
            if (subdir / "dist").exists():
                shutil.rmtree(subdir / "dist")
            for distdir in subdir.glob("*.dist-info"):
                shutil.rmtree(distdir)
            for distdir in subdir.glob("*.egg-info"):
                shutil.rmtree(distdir)

    def assert_has_edge(self, mg, from_name, to_name, edge_data):
        self.assert_has_node(mg, from_name)
        self.assert_has_node(mg, to_name)

        try:
            edge = mg.edge_data(from_name, to_name)

        except KeyError:
            pass
        else:
            if edge_data is not None:
                self.assertEqual(len(edge), len(edge_data))
                self.assertEqual(edge, edge_data)
            return

        self.fail(f"No edge between {from_name!r} and {to_name!r}")

    def assert_has_node(self, mg, node, node_type=None):
        value = mg.find_node(node)
        self.assertIsNot(value, None)
        if node_type is not None:
            self.assertTrue(isinstance(value, node_type))

    def test_package(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            build_and_install(INPUT_DIR / "full-package", tmpdir)

            with prefixed_sys_path(tmpdir):
                mg = modulegraph2.ModuleGraph()
                mg.add_module("package")

                self.assert_has_node(mg, "package", modulegraph2.Package)
                self.assertTrue(
                    isinstance(
                        mg.find_node("package").init_module,
                        modulegraph2.ExtensionModule,
                    )
                )
                self.assert_has_node(mg, "package.sub", modulegraph2.ExtensionModule)
                self.assert_has_node(mg, "package.mod", modulegraph2.ExtensionModule)
                self.assertIs(mg.find_node("package.mod1"), None)

                self.assert_has_edge(
                    mg,
                    "package",
                    "pathlib",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.sub",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.mod",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )

                self.assert_has_edge(
                    mg,
                    "package.sub",
                    "os",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package.mod",
                    "sqlite3",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )

                for node in mg.nodes():
                    if node.identifier.endswith("__mypyc"):
                        self.assert_has_edge(mg, "package", node.identifier, None)
                        self.assert_has_edge(mg, "package.sub", node.identifier, None)
                        self.assert_has_edge(mg, "package.mod", node.identifier, None)

    def test_package_plain_init(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            build_and_install(INPUT_DIR / "plain-init-package", tmpdir)

            with prefixed_sys_path(tmpdir):
                mg = modulegraph2.ModuleGraph()
                mg.add_module("package")

                self.assert_has_node(mg, "package", modulegraph2.Package)
                self.assertTrue(
                    isinstance(
                        mg.find_node("package").init_module,
                        modulegraph2.SourceModule,
                    )
                )
                self.assert_has_node(mg, "package.sub", modulegraph2.ExtensionModule)
                self.assert_has_node(mg, "package.mod", modulegraph2.ExtensionModule)
                self.assertIs(mg.find_node("package.mod1"), None)

                self.assert_has_edge(
                    mg,
                    "package",
                    "pathlib",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.sub",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.mod",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )

                self.assert_has_edge(
                    mg,
                    "package.sub",
                    "os",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package.mod",
                    "sqlite3",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )

                for node in mg.nodes():
                    if node.identifier.endswith("__mypyc"):
                        try:
                            mg.edge_data("package", node.identifier)
                        except KeyError:
                            pass
                        else:
                            self.fail("Unexpected edge from source module to helper")
                        self.assert_has_edge(mg, "package.sub", node.identifier, None)
                        self.assert_has_edge(mg, "package.mod", node.identifier, None)

    def test_partial_package(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            build_and_install(INPUT_DIR / "partial-package", tmpdir)

            with prefixed_sys_path(tmpdir):
                mg = modulegraph2.ModuleGraph()
                mg.add_module("package")

                self.assert_has_node(mg, "package", modulegraph2.Package)
                self.assertTrue(
                    isinstance(
                        mg.find_node("package").init_module,
                        modulegraph2.ExtensionModule,
                    )
                )
                self.assert_has_node(mg, "package.sub", modulegraph2.ExtensionModule)
                self.assert_has_node(mg, "package.mod", modulegraph2.SourceModule)
                self.assertIs(mg.find_node("package.mod1"), None)

                self.assert_has_edge(
                    mg,
                    "package",
                    "pathlib",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.sub",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package",
                    "package.mod",
                    {modulegraph2.DependencyInfo(False, True, True, None)},
                )

                self.assert_has_edge(
                    mg,
                    "package.sub",
                    "os",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )
                self.assert_has_edge(
                    mg,
                    "package.mod",
                    "sqlite3",
                    {modulegraph2.DependencyInfo(False, True, False, None)},
                )

                for node in mg.nodes():
                    if node.identifier.endswith("__mypyc"):
                        self.assert_has_edge(mg, "package", node.identifier, None)
                        self.assert_has_edge(mg, "package.sub", node.identifier, None)

                        try:
                            mg.edge_data("package.mod", node.identifier)
                        except KeyError:
                            pass
                        else:
                            self.fail("Unexpected edge from source module to helper")

    def test_package_no_source(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            build_and_install(INPUT_DIR / "full-package", tmpdir)

            for nm in pathlib.Path(tmpdir).glob("*/*.py"):
                nm.unlink()

            with prefixed_sys_path(tmpdir):
                mg = modulegraph2.ModuleGraph()
                mg.add_module("package")

                self.assert_has_node(mg, "package", modulegraph2.Package)
                self.assertTrue(
                    isinstance(
                        mg.find_node("package").init_module,
                        modulegraph2.ExtensionModule,
                    )
                )

                # No sources, hence dependencies cannot be found
                self.assertIs(mg.find_node("package.sub"), None)
                self.assertIs(mg.find_node("package.mod"), None)
                self.assertIs(mg.find_node("package.mod1"), None)
