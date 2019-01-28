modulegraph2 reference documentation
====================================

.. automodule:: modulegraph2

Graph
.....

.. autoclass:: modulegraph2.ModuleGraph

Creating the graph
~~~~~~~~~~~~~~~~~~

.. automethod:: modulegraph2.ModuleGraph.__init__

.. automethod:: modulegraph2.ModuleGraph.add_module

.. automethod:: modulegraph2.ModuleGraph.add_script

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

.. autoclass:: modulegraph2.Module
   :members:

.. autoclass:: modulegraph2.BuiltinModule
   :members:

.. autoclass:: modulegraph2.BytecodeModule
   :members:

.. autoclass:: modulegraph2.ExtensionModule
   :members:

.. autoclass:: modulegraph2.FrozenModule
   :members:

.. autoclass:: modulegraph2.SourceModule
   :members:

.. autoclass:: modulegraph2.NamespacePackage
   :members:

.. autoclass:: modulegraph2.Package
   :members:

.. autoclass:: modulegraph2.Script
   :members:


Special nodes
~~~~~~~~~~~~~

.. autoclass:: modulegraph2.AliasNode
   :members:

.. autoclass:: modulegraph2.ExcludedModule
   :members:

.. autoclass:: modulegraph2.MissingModule
   :members:

.. autoclass:: modulegraph2.InvalidRelativeImport
   :members:

Node and link attributes
........................

.. autoclass:: modulegraph2.DependencyInfo


Distributions
.............

.. autoclass:: modulegraph2.PyPIDistribution
   :members:

.. autofunction:: modulegraph2.distribution_named

.. autofunction:: modulegraph2.all_distributions


Utilities
.........

.. autofunctions:: modulegraph2.saved_sys_path
