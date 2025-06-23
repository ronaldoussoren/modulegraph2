"""
Support code that deals with packages compiled
with mypyc.
"""

import ast

import modulegraph2

from ._ast_tools import extract_ast_info
from ._depinfo import DependencyInfo
from ._nodes import BaseNode, ExtensionModule, Package

# Mypyc compiles Python code in a package to extension
# modules, but generally leaves the Python sources next
# to those extension.
#
# Use this to update the dependency graph.
#
# A package compiled with mypy can be detected by
# looking for a toplevel module whose name starts
# with a hex string and ends with ``__mypyc``.
#
# The code tries to be careful and does not add
# dependencies when it cannot find the python sources
# corresponding to the extension module.


def mypyc_post_processing_hook(graph: "modulegraph2.ModuleGraph", node: BaseNode):
    # Look for extension modules, but standalone and
    # as the ``__init__`` for a package.
    if isinstance(node, Package):
        if not isinstance(node.init_module, ExtensionModule):
            return
    elif not isinstance(node, ExtensionModule):
        return

    # Only look at nodes with a distribution, uninstalled
    # modules don't have the information this hook needs.
    if node.distribution is None:
        return

    # This function will try to parse the source
    # file next to the node in the filesystem, that
    # requires knowing the filename for the node.
    if isinstance(node, Package):
        if node.init_module.filename is None:  # pragma: no branch
            # This should never happen, a package that
            # was not loaded from something filesystem-like
            return  # pragma: no cover
        else:
            source_filename = node.init_module.filename.parent / (
                node.init_module.filename.stem.split(".", 1)[0] + ".py"
            )

    elif node.filename is None:  # pragma: no branch
        # This should never happen: A installed distribution
        # but without a filesystem location.
        return  # pragma: no cover
    else:
        source_filename = node.filename.parent / (
            node.filename.stem.split(".", 1)[0] + ".py"
        )

    # Finally check that the distribution appears to
    # be compiled with mypyc.
    #
    # The name check can be made stricter if needed
    # by looking at the prefix as well.
    for nm in node.distribution.import_names:
        if nm.endswith("__mypyc"):
            # Distribution is mypyc compiled
            helper_module = nm
            break
    else:
        # Distribution is not mypyc compiled
        return

    # Locate the source code that's next to the extension module.
    #
    # This code assumes that the extension module is in the filesystem,
    # which should be good enough in practice (AFAIK none of the major
    # platforms support loading extension modules from memory).
    if not source_filename.is_file():
        return

    # Add explicit dependency to the mypy helper extension module
    helper_node = graph.add_module(helper_module)
    graph.add_edge(node, helper_node, DependencyInfo(False, True, False, None))

    source_code = source_filename.read_bytes()

    try:
        ast_node = compile(
            source_code,
            str(source_filename),
            "exec",
            flags=ast.PyCF_ONLY_AST,
            dont_inherit=True,
        )
    except SyntaxError:
        return

    else:
        imports = list(extract_ast_info(ast_node))

    # And finally process the dependencies found in the source file.
    if imports:
        graph._process_import_list(node, imports)
        graph._run_stack()
