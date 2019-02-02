modulegraph2 reference documentation
====================================

.. automodule:: modulegraph2

.. contents::
   :depth: 3

Graph
.....

.. autoclass:: modulegraph2.ModuleGraph

Creating the graph
~~~~~~~~~~~~~~~~~~

.. automethod:: modulegraph2.ModuleGraph.__init__

.. automethod:: modulegraph2.ModuleGraph.add_module

.. automethod:: modulegraph2.ModuleGraph.add_script

.. automethod:: modulegraph2.ModuleGraph.add_distribution

Affecting building the graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: modulegraph2.ModuleGraph.add_excludes

.. automethod:: modulegraph2.ModuleGraph.add_implies

Callbacks
~~~~~~~~~

.. automethod:: modulegraph2.ModuleGraph.add_missing_hook

.. automethod:: modulegraph2.ModuleGraph.add_post_processing_hook

Reporting
~~~~~~~~~

.. automethod:: modulegraph2.ModuleGraph.distributions

.. automethod:: modulegraph2.ModuleGraph.report

Graph Nodes
...........

The graph can contain nodes of a number of classes, as described
below. All these classes are :class:`dataclasses <dataclasses.dataclass>`.

.. autoclass:: modulegraph2.BaseNode
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.Module
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.BuiltinModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.BytecodeModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.ExtensionModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.FrozenModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.SourceModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.NamespacePackage
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.Package
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.Script
   :members:
   :show-inheritance:


Special nodes
~~~~~~~~~~~~~

.. autoclass:: modulegraph2.VirtualNode
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.AliasNode
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.ExcludedModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.MissingModule
   :members:
   :show-inheritance:

.. autoclass:: modulegraph2.InvalidRelativeImport
   :members:
   :show-inheritance:

Edge attributes
................

.. autoclass:: modulegraph2.DependencyInfo


Distributions
.............

.. autoclass:: modulegraph2.PyPIDistribution
   :members:

.. autofunction:: modulegraph2.distribution_named

.. autofunction:: modulegraph2.all_distributions


Utilities
.........

.. autofunction:: modulegraph2.saved_sys_path


.. class:: modulegraph2.Alias

.. class:: modulegraph2.Virtual
