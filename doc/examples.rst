Examples
========

Basic usage
...........

.. sourcecode:: python

   import modulegraph2

   mg = modulegraph2.ModuleGraph()
   mg.add_module("sys")

   mg.find_node("sys")
   # modulegraph2.BuiltinModule("sys")

   mg.find_node("os")
   # None
