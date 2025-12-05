Modulegraph2 - Python module dependency graph
=============================================

.. rst-class:: lead

   Modulegraph2 is a library for creating and introspecting
   the dependency graph between Python modules. The graph is
   created using static analisys from source and byte code.

   The dependency graph contains information about packages,
   modules, extensions and their dependencies. The dependencies
   are annotated with relevant information about the import
   statement.

   Modules that from a distribution installed using pip also have
   a link to information about that distribution.

.. container:: buttons

   `GitHub <https://github.com/ronaldoussoren/pyobjc>`_

.. grid:: 1 1 2 3
   :gutter: 2
   :padding:  0
   :class-row: surface

   .. grid-item-card:: Release Info
      :link: changelog
      :link-type: doc

      modulegraph 2.3  was released on 2025-11-23.  See the :doc:`changelog <changelog>` for more information.


   .. grid-item-card:: Supported Platforms

      - Python 3.10 and later

   .. grid-item-card:: Installing modulegraph2

      .. sourcecode:: sh

         $ python3 -mpip \
           install -U modulegraph2

.. toctree::
   :hidden:

   changelog

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card::

      .. toctree::
         :caption: Using
         :maxdepth: 1

         command-line
         modulegraph2
         examples

   .. grid-item-card::

      .. toctree::
         :caption: Development
         :maxdepth: 1

         license
         development
         internals
