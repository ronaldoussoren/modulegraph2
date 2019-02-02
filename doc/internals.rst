Modulegraph2 internals
======================

.. warning::

   Everything documented in this file is private to the implementation
   of modulegraph and should not be relied on by users of the module.

   Please file and issue if you do need functionality documented here,
   and include the use case you need the functionality for.

Package structure
-----------------

The modulegraph2 package contains a number of submodules that
actually implement the behavior, with code separated in logical
modules.

All submodules with a name that start with an underscore are
private, and that's also true for all names defined in those
modules unless they are explicitly exported by the package
``__init__.py`` file.

.. contents::
   :depth: 2

Module "_ast_tools": working with the AST for a module
------------------------------------------------------

.. automodule:: modulegraph2._ast_tools
   :members:
   :undoc-members:
   :private-members:

Module "_bytecode_tools": working with the bytecode for a module
----------------------------------------------------------------

.. automodule:: modulegraph2._bytecode_tools
   :members:
   :undoc-members:
   :private-members:

Module "_callback_list": working with lists of callbacks
--------------------------------------------------------

.. automodule:: modulegraph2._callback_list
   :members:
   :undoc-members:
   :private-members:
   :special-members: __call__

Module "_depinfo": information about a dependency
-------------------------------------------------

.. automodule:: modulegraph2._depinfo

Public API
..........

This module defines the following public API:

* :class:`modulegraph2.DependencyInfo`

Private API
...........

.. autofunction:: modulegraph2._depinfo.from_importinfo


Module "_distributions": Package distributions
----------------------------------------------

.. automodule:: modulegraph2._distributions

Public API
..........

This module defines the following public API:

* :class:`modulegraph2.PyPIDistribution`

* :func:`modulegraph2.all_distributions`

* :func:`modulegraph2.distribution_named`

Private API
...........

.. data:: modulegraph2._distributions._cached_distributions

   Global variable used by :func:`modulegraph2.all_distributions` to
   cache the distributions found on :data:`sys.path`. This is used both
   for performance and to ensure module graphs end up with one
   :class:`PyPIDistribution` per distribution found.

.. autofunction:: modulegraph2._distributions.create_distribution

.. autofunction:: modulegraph2._distributions.distribution_for_file


.. autofunction:: modulegraph2._depinfo.from_importinfo

Module "_dotbuilder": Outputting graphviz files
-----------------------------------------------

.. automodule:: modulegraph2._dotbuilder
   :members:
   :undoc-members:
   :private-members:

Module "_graphbuilder": Support functions for building dependency graphs
------------------------------------------------------------------------

.. automodule:: modulegraph2._graphbuilder
   :members:
   :undoc-members:
   :private-members:

Module "_htmlbuilder": Outputting HTML files
--------------------------------------------

.. automodule:: modulegraph2._htmlbuilder
   :members:
   :undoc-members:
   :private-members:

Module "_implies": Implied dependencies for stdlib
--------------------------------------------------

.. automodule:: modulegraph2._implies

   .. autoclass:: Alias
      :members:

   .. autodata:: STDLIB_IMPLIES
      :annotation:

   .. autodata:: STDLIB_PLATFORM_IMPLIES
      :annotation:

   .. autodata:: STDLIB_VERSION_IMPLIES
      :annotation:

Module "_importinfo": Information about edges in the dependency graph
---------------------------------------------------------------------

.. automodule:: modulegraph2._importinfo
   :members:
   :undoc-members:

Module "_modulegraph": The main module graph and builder
--------------------------------------------------------

.. automodule:: modulegraph2._modulegraph

Public API
..........

This module defines the following public API:

* :class:`modulegraph2.ModuleGraph`

Private API
...........

.. autodata:: modulegraph2._modulegraph.ProcessingCallback
   :annotation:

.. autodata:: modulegraph2._modulegraph.MissingCallback
   :annotation:

.. autodata:: modulegraph2._modulegraph.DEFAULT_DEPENDENCY
   :annotation:



The ModuleGraph class also contains private methods,
documented below:

.. automethod:: modulegraph2.ModuleGraph._create_missing_module
.. automethod:: modulegraph2.ModuleGraph._run_stack
.. automethod:: modulegraph2.ModuleGraph._implied_references
.. automethod:: modulegraph2.ModuleGraph._load_module
.. automethod:: modulegraph2.ModuleGraph._load_script
.. automethod:: modulegraph2.ModuleGraph._process_import_list
.. automethod:: modulegraph2.ModuleGraph._find_or_load_module
.. automethod:: modulegraph2.ModuleGraph._process_import
.. automethod:: modulegraph2.ModuleGraph._process_namelist

Building the graph
..................

The graph building algorithm explictly manages a work stack
to avoid exhausting the stack. This is a work stack because
imports need to be processed depth first to be able to
process ``from ... import ...`` statements correctly.

The diagram below is an overview of the imported method
interactions while building a dependecy graph.

.. blockdiag::

   blockdiag callgraph {
     add_module -> _find_or_load_module
     add_script -> _find_or_load_module

     _find_or_load_module -> _find_or_load_module
     _find_or_load_module -> _implied_references
     _find_or_load_module -> _load_module

     _implied_references -> _find_or_load_module

     _load_module -> _create_missing_module
     _load_module -> _process_import_list

     _process_import_list -> _process_import
     _process_import_list -> _post_processing

     _process_import -> _find_or_load_module
     _process_import -> _process_namelist

     _process_namelist -> _find_or_load_module
   }

The call graph implies recursion through *_find_or_load_module*, but
that recursion is managed explicitly through a work stack that is
processed iteratively. The intention is to avoid exhausting the stack
with convoluted code bases.

Module "_nodes": Definition of graph nodes
------------------------------------------

.. automodule:: modulegraph2._nodes

Public API
..........

This module defines the following public API:

* :class:`modulegraph2.AliasNode`
* :class:`modulegraph2.BaseNode`
* :class:`modulegraph2.BuiltinModule`
* :class:`modulegraph2.BytecodeModule`
* :class:`modulegraph2.ExcludedModule`
* :class:`modulegraph2.ExtensionModule`
* :class:`modulegraph2.FrozenModule`
* :class:`modulegraph2.MissingModule`
* :class:`modulegraph2.Module`
* :class:`modulegraph2.NamespacePackage`
* :class:`modulegraph2.Package`
* :class:`modulegraph2.Script`
* :class:`modulegraph2.SourceModule`
* :class:`modulegraph2.InvalidRelativeImport`

Private API
...........

This module does not have a private API.


Module "_swig_support": Hooks for dealing with SWIG
---------------------------------------------------

.. automodule:: modulegraph2._swig_support
   :members:
   :undoc-members:
   :private-members:

Module "_utilities": Definition of graph nodes
----------------------------------------------

.. automodule:: modulegraph2._utilities

Public API
..........

This module defines the following public API:

* :class:`modulegraph2.saved_sys_path`

Private API
...........

.. autofunction:: modulegraph2._utilities.split_package

.. autoclass:: modulegraph2._utilities.FakePackage
