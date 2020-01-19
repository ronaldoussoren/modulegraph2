Modulegraph2 - Python module dependency graph
=============================================

Modulegraph2 is a library for creating and introspecting
the dependency graph between Python modules. The graph is
created using static analisys from source and byte code.

The dependency graph contains information about packages,
modules, extensions and their dependencies. The dependencies
are annotated with relevant information about the import
statement.

Modules that from a distribution installed using `pip`_ also have
a link to information about that distribution.


Release information
-------------------

Modulegraph2 2.0a1 was released on 2019-02-03. See the :doc:`changelog <changelog>`
for information on this release.


Installation
------------

Modulegraph2 can be installed using `pip <https://pypi.org/project/pip/>`_.


Supported platforms
-------------------

Modulegraph2 supports Python 3.6 and later on all platforms. The code
is developed using Python 3.7 on macOS, but and regularly tested with
other Python versions and on Linux and Windows.

Windows and Linux build status:

.. image:: https://ci.appveyor.com/api/projects/status/ru71tpdinlr7whym?svg=true
   :target: https://ci.appveyor.com/project/RonaldOussoren/modulegraph2

Using modulegraph2
------------------

.. toctree::
   :maxdepth: 1

   command-line
   modulegraph2
   examples


Development
-----------

.. toctree::
   :maxdepth: 1

   license
   changelog
   development
   internals

Online Resources
................

* `Sourcecode repository on GitHub <https://github.com/ronaldoussoren/modulegraph2/>`_

* `The issue tracker <https://github.com/ronaldoussoren/modulegraph2/issues>`_
